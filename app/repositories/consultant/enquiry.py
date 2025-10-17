from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models.consultant.consultant_enquiry import ConsultantEnquiry
from app.core.exceptions import AlreadyExistsError

class ConsultantEnquiryRepository:
    @staticmethod
    async def get_by_email(db: AsyncSession, email: str) -> ConsultantEnquiry:
        """Check if enquiry with email already exists"""
        query = select(ConsultantEnquiry).where(ConsultantEnquiry.email == email)
        result = await db.execute(query)
        return result.scalar_one_or_none()
    
    @staticmethod
    async def create(db: AsyncSession, enquiry_data: dict) -> ConsultantEnquiry:
        # Check if email already exists
        existing_enquiry = await ConsultantEnquiryRepository.get_by_email(db, enquiry_data["email"])
        if existing_enquiry:
            raise AlreadyExistsError("This email is already registered")
        
        enquiry = ConsultantEnquiry(
            full_name=enquiry_data["full_name"],
            email=enquiry_data["email"],
            phone=enquiry_data["phone"],
            message=enquiry_data["message"],
            qualification_id=enquiry_data["qualification_id"],
            languages=enquiry_data["regional_languages"]
        )
        db.add(enquiry)
        await db.commit()
        await db.refresh(enquiry)
        return enquiry
