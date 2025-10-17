from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.services.masters.qualification import QualificationService
from app.utils.response_helper import success_response, error_response
from app.schemas.response_schema import ResponseSchema

router = APIRouter(prefix="/qualifications", tags=["Qualifications"])

@router.get("/", response_model=ResponseSchema, status_code=status.HTTP_200_OK)
async def list_qualifications(db: AsyncSession = Depends(get_db)):
    try:
        qualifications = await QualificationService.list_qualifications(db)
        data = [{"id": qual.id, "name": qual.name} for qual in qualifications]
        return success_response("Qualifications fetched successfully", data, status_code=200)
    except Exception as e:
        return error_response(f"Error fetching qualifications: {str(e)}", status_code=500)
