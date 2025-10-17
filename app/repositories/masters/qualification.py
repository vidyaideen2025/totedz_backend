from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models.masters.qualifications import Qualification

class QualificationRepository:
    @staticmethod
    async def get_all_qualifications(db: AsyncSession):
        query = select(Qualification.id, Qualification.name).order_by(Qualification.name)
        result = await db.execute(query)
        return result.all()
