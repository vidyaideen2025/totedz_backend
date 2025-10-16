from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, Boolean, func, String
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4

class BaseModel:
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    is_deleted = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)

Base = declarative_base(cls=BaseModel)