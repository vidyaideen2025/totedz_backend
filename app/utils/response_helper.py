from app.schemas.response_schema import ResponseSchema

def success_response(message: str, result=None, status_code: int = 200):
    return ResponseSchema(
        status="success",
        message=message,
        status_code=status_code,
        result=result
    )

def error_response(message: str, status_code: int, result=None):
    return ResponseSchema(
        status="error",
        message=message,
        status_code=status_code,
        result=result
    )
