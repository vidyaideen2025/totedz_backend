from typing import Any, Optional
from pydantic import BaseModel

class ResponseSchema(BaseModel):
    status_code: int  # HTTP code (e.g., 200, 404, 500)
    status: str  # "success" or "error"
    message: str
    result: Optional[Any] = None
