from sqlalchemy import select

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.organization import Organization


class OrganizationRepository:

    @staticmethod
    async def create_organization(
        db: AsyncSession,
        organization: Organization
    ):

        db.add(organization)

        await db.commit()

        await db.refresh(organization)

        return organization

    @staticmethod
    async def get_by_id(
        db: AsyncSession,
        organization_id: str
    ):

        result = await db.execute(
            select(Organization).where(
                Organization.id == organization_id
            )
        )

        return result.scalar_one_or_none()

    @staticmethod
    async def get_all(
        db: AsyncSession
    ):

        result = await db.execute(
            select(Organization)
        )

        return result.scalars().all()