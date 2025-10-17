from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from uuid import uuid4
from app.db.base import Base

class User(Base):
    __tablename__ = "users"
    
    STUDENT = 1
    CONSULTANT = 2
    ADMIN = 3

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    email = Column(String, nullable=False, unique=True, index=True)
    password_hash = Column(String, nullable=False)
    role_id = Column(UUID(as_uuid=True), ForeignKey("roles.id"), nullable=False)
    user_type = Column(Integer, nullable=False, default=CONSULTANT)
    is_consultant = Column(Boolean, default=False)
    is_verified = Column(Boolean, default=False)
    is_email_verified = Column(Boolean, default=False)
    is_phone_verified = Column(Boolean, default=False)
    
    role = relationship("Role", back_populates="users")
    consultant_enquiries = relationship("ConsultantEnquiry", foreign_keys="[ConsultantEnquiry.user_id]", back_populates="user", lazy="select")


    
    
    
   
