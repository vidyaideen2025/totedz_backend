from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models.masters.languages import Language

class LanguageRepository:
    @staticmethod
    async def get_all_languages(db: AsyncSession):
        query = select(Language.id, Language.name).order_by(Language.name)
        result = await db.execute(query)
        return result.all()
