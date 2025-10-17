from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.consultant.enquiry import ConsultantEnquiryRepository

class ConsultantEnquiryService:
    @staticmethod
    async def submit_enquiry(db: AsyncSession, enquiry_data: dict):
        return await ConsultantEnquiryRepository.create(db, enquiry_data)
