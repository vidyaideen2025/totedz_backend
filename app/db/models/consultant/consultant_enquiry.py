from sqlalchemy import Column, String, Integer, ForeignKey, Boolean, Text, ARRAY
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
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
    qualification_id = Column(UUID(as_uuid=True), ForeignKey("qualifications.id"))
    languages = Column(ARRAY(UUID(as_uuid=True)))
    status = Column(Boolean, default=False)
    license_id = Column(Text, nullable=True)
    verified_by_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=True)
    is_email_verified = Column(Boolean, default=False)
    is_phone_verified = Column(Boolean, default=False)

    # Relationships - using lazy loading to avoid circular imports
    # user_id is nullable - will be set after admin approves and creates user account
    user = relationship("User", foreign_keys="[ConsultantEnquiry.user_id]", back_populates="consultant_enquiries", lazy="select")
    qualification = relationship("Qualification", lazy="select")
    verified_by = relationship("User", foreign_keys="[ConsultantEnquiry.verified_by_id]", lazy="select")



    
    
