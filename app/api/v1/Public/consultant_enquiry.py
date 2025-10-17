from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.consultant.enquiry import ConsultantEnquiryCreate
from app.services.consultant.enquiry import ConsultantEnquiryService
from app.utils.response_helper import success_response
from app.db.session import get_db
from app.schemas.response_schema import ResponseSchema

router = APIRouter(prefix="/consultant-enquiries", tags=["Consultant Enquiries"])

@router.post("/", response_model=ResponseSchema, status_code=status.HTTP_201_CREATED)
async def submit_consultant_enquiry(
    payload: ConsultantEnquiryCreate,
    db: AsyncSession = Depends(get_db)
):
    """
    Submit a consultant enquiry. All fields are mandatory.
    """
    enquiry = await ConsultantEnquiryService.submit_enquiry(db, payload.model_dump())
    return success_response(
        "Enquiry submitted successfully",
        {
            "id": str(enquiry.id),
            "full_name": enquiry.full_name,
            "email": enquiry.email,
            "phone": enquiry.phone,
            "message": enquiry.message,
            "qualification_id": str(enquiry.qualification_id),
            "regional_languages": [str(lang) for lang in enquiry.languages],
            "status": enquiry.status
        },
        status_code=201
    )
