from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.services.masters.language import LanguageService
from app.utils.response_helper import success_response, error_response
from app.schemas.response_schema import ResponseSchema

router = APIRouter(prefix="/languages", tags=["Languages"])

@router.get("/", response_model=ResponseSchema, status_code=status.HTTP_200_OK)
async def list_languages(db: AsyncSession = Depends(get_db)):
    try:
        languages = await LanguageService.list_languages(db)
        data = [{"id": lang.id, "name": lang.name} for lang in languages]
        return success_response("Languages fetched successfully", data, status_code=200)
    except Exception as e:
        return error_response(f"Error fetching languages: {str(e)}", status_code=500)
