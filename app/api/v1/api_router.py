from fastapi import APIRouter, FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi import HTTPException

from app.api.v1.Public.language import router as language_router
from app.api.v1.Public.qualification import router as qualification_router
from app.api.v1.Public.consultant_enquiry import router as consultant_enquiry_router
from app.core.exceptions import AppException
from app.core.exception_handlers import (
    app_exception_handler,
    http_exception_handler,
    validation_exception_handler,
    global_exception_handler
)

# Central router (can mount multiple routers)
api_router = APIRouter()

# Include all route modules
api_router.include_router(language_router)
api_router.include_router(qualification_router)
api_router.include_router(consultant_enquiry_router)

# Function to register all routers & exception handlers to app
def register_app(app: FastAPI):
    app.include_router(api_router)
    
    # Exception handlers (order matters - most specific first)
    app.add_exception_handler(AppException, app_exception_handler)
    app.add_exception_handler(HTTPException, http_exception_handler)
    app.add_exception_handler(RequestValidationError, validation_exception_handler)
    app.add_exception_handler(Exception, global_exception_handler)
