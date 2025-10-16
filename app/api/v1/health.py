from fastapi import APIRouter

router = APIRouter(prefix="/health", tags=["Health"])


@router.get("")
async def health_check():
    """
    Health check endpoint
    Returns the status of the API
    """
    return {
        "status": "healthy",
        "message": "API is running"
    }
