from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import base, relationship
from uuid import uuid4
from app.db.base import Base


class Role(Base):
    __tablename__ = "roles"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String, nullable=False, unique=True, index=True)
    description = Column(String, nullable=False)

    users = relationship("User", back_populates="role")
    
