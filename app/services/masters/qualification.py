from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.masters.qualification import QualificationRepository

class QualificationService:
    @staticmethod
    async def list_qualifications(db: AsyncSession):
        return await QualificationRepository.get_all_qualifications(db)
