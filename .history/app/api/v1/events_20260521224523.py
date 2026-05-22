from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db

from app.dependencies.auth import get_current_user

from app.models.user import User

from app.schemas.event import (
    EventCreate,
    EventResponse
)

from app.services.event_service import EventService

from app.utils.csv_parser import parse_csv_events


router = APIRouter(
    prefix="/events",
    tags=["Events"]
)


@router.post(
    "/",
    response_model=EventResponse
)
async def ingest_event(
    payload: EventCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    event = await EventService.ingest_event(
        db,
        payload,
        current_user.organization_id
    )

    return event


@router.post("/batch")
async def ingest_batch_events(
    payloads: list[EventCreate],
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    events = []

    for payload in payloads:

        event = await EventService.ingest_event(
            db,
            payload,
            current_user.organization_id
        )

        events.append(event)

    return {
        "message": "Batch events ingested",
        "count": len(events)
    }


@router.post("/upload-csv")
async def upload_csv(
    file: UploadFile = File(...),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    # Validate file type

    if not file.filename.endswith(".csv"):

        raise HTTPException(
            status_code=400,
            detail="Only CSV files are allowed"
        )

    # Read CSV

    contents = await file.read()

    events = parse_csv_events(
        contents.decode("utf-8")
    )

    created_events = []

    for item in events:

        payload = EventCreate(
            event_name=item["event_name"],
            event_type=item["event_type"],
            source=item["source"],
            properties=item["properties"]
        )

        event = await EventService.ingest_event(
            db,
            payload,
            current_user.organization_id
        )

        created_events.append(event)

    return {
        "message": "CSV uploaded successfully",
        "events_created": len(created_events),
        "filename": file.filename
    }


@router.get(
    "/",
    response_model=list[EventResponse]
)
async def get_events(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return await EventService.get_events(
        db,
        current_user.organization_id
    )