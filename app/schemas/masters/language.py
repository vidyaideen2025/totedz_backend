from pydantic import BaseModel
from uuid import UUID

class LanguageOut(BaseModel):
    id: UUID
    name: str

    class Config:
        orm_mode = True
