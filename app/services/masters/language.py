from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.masters.language import LanguageRepository

class LanguageService:
    @staticmethod
    async def list_languages(db: AsyncSession):
        return await LanguageRepository.get_all_languages(db)
