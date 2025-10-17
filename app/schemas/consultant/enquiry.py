from pydantic import BaseModel, Field, EmailStr
from typing import List
from uuid import UUID

class ConsultantEnquiryCreate(BaseModel):
    full_name: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    phone: str = Field(..., min_length=10, max_length=15)
    message: str = Field(..., min_length=5, max_length=1000)
    qualification_id: UUID
    regional_languages: List[UUID] = Field(..., min_items=1)
