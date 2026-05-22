from sqlalchemy import select

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User
from app.models.organization import Organization

from app.schemas.auth import (
    RegisterRequest,
    LoginRequest
)

from app.repositories.user_repository import UserRepository
from app.repositories.org_repository import (
    OrganizationRepository
)

from app.core.security import (
    hash_password,
    verify_password,
    create_access_token
)


class AuthService:

    @staticmethod
    async def register(
        db: AsyncSession,
        payload: RegisterRequest
    ):

        # Check existing user

        existing_user = await UserRepository.get_by_email(
            db,
            payload.email
        )

        if existing_user:

            raise Exception(
                "User already exists"
            )

        # Generate slug

        slug = payload.organization_name.lower().replace(
            " ",
            "-"
        )

        # Check existing organization

        result = await db.execute(
            select(Organization).where(
                Organization.slug == slug
            )
        )

        organization = result.scalar_one_or_none()

        # Create organization only if not exists

        if not organization:

            organization = Organization(
                name=payload.organization_name,
                slug=slug,
                owner_id=None
            )

            organization = await OrganizationRepository.create_organization(
                db,
                organization
            )

        # Create user

        user = User(
            email=payload.email,
            hashed_password=hash_password(
                payload.password
            ),
            full_name=payload.full_name,
            role="OWNER",
            organization_id=organization.id
        )

        await UserRepository.create_user(
            db,
            user
        )

        # Update owner_id if empty

        if not organization.owner_id:

            organization.owner_id = str(user.id)

            await db.commit()

        # Generate token

        token = create_access_token(
            {"sub": user.email}
        )

        return {
            "access_token": token,
            "refresh_token": token,
            "token_type": "bearer"
        }

    @staticmethod
    async def login(
        db: AsyncSession,
        payload: LoginRequest
    ):

        user = await UserRepository.get_by_email(
            db,
            payload.email
        )

        if not user:

            raise Exception(
                "Invalid credentials"
            )

        if not verify_password(
            payload.password,
            user.hashed_password
        ):

            raise Exception(
                "Invalid credentials"
            )

        token = create_access_token(
            {"sub": user.email}
        )

        return {
            "access_token": token,
            "refresh_token": token,
            "token_type": "bearer"
        }