from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from uuid import uuid4
from app.db.base import Base


class Qualification(Base):
    __tablename__ = "qualifications"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String, nullable=False, unique=True, index=True)
    description = Column(String, nullable=False)
    
    consultant_enquiry = relationship("ConsultantEnquiry", back_populates="qualification")
