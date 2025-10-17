from sqlalchemy import Column, String, Integer, ForeignKey, Boolean, Text, ARRAY
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import base, relationship
from uuid import uuid4
from app.db.base import Base


class ConsultantEnquiry(Base):
    __tablename__ = "consultant_enquiry"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=True)
    full_name = Column(String, nullable=False, index=True)
    email = Column(String, nullable=False, index=True)
    phone = Column(String, nullable=False, index=True)
    message = Column(Text, nullable=False)
    qualification = Column(UUID(as_uuid=True), ForeignKey("qualifications.id"))
    languages = Column(ARRAY(UUID(as_uuid=True)))
    status = Column(Boolean, default=False)
    license_id = Column(Text, nullable=True)
    verified_by = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=True)
    is_email_verified = Column(Boolean, default=False)
    is_phone_verified = Column(Boolean, default=False)

    user = relationship("User", back_populates="consultant_enquiry")
    qualification = relationship("Qualification", back_populates="consultant_enquiry")
    verified_by = relationship("User", back_populates="verified_consultant_enquiry")




    
    
