from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File


router = APIRouter(
    prefix="/events",
    tags=["Events"]
)


@router.post("/")
async def ingest_event():

    return {
        "message": "Single event ingested"
    }


@router.post("/batch")
async def ingest_batch_events():

    return {
        "message": "Batch events ingested"
    }


@router.post("/upload-csv")
async def upload_csv(
    file: UploadFile = File(...)
):

    return {
        "filename": file.filename
    }