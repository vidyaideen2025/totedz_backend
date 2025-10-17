from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from app.utils.response_helper import error_response
from app.core.exceptions import AppException

async def app_exception_handler(request: Request, exc: AppException):
    """Handle custom application exceptions"""
    response = error_response(message=exc.message, status_code=exc.status_code)
    return JSONResponse(status_code=exc.status_code, content=response.model_dump())

async def http_exception_handler(request: Request, exc: HTTPException):
    response = error_response(message=str(exc.detail), status_code=exc.status_code)
    return JSONResponse(status_code=exc.status_code, content=response.model_dump())

async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = [
        {"field": e["loc"][-1], "message": e["msg"]}
        for e in exc.errors()
    ]
    response = error_response(message="Validation Error", status_code=422, result=errors)
    return JSONResponse(status_code=422, content=response.model_dump())

async def global_exception_handler(request: Request, exc: Exception):
    response = error_response(message="Internal Server Error", status_code=500, result=str(exc))
    return JSONResponse(status_code=500, content=response.model_dump())
