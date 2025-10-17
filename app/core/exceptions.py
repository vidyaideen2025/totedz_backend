"""
Custom exceptions for the application
"""

class AppException(Exception):
    """Base exception for all application exceptions"""
    def __init__(self, message: str, status_code: int = 400):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)


class ValidationError(AppException):
    """Raised when validation fails"""
    def __init__(self, message: str):
        super().__init__(message, status_code=400)


class NotFoundError(AppException):
    """Raised when resource is not found"""
    def __init__(self, message: str):
        super().__init__(message, status_code=404)


class AlreadyExistsError(AppException):
    """Raised when resource already exists"""
    def __init__(self, message: str):
        super().__init__(message, status_code=409)


class UnauthorizedError(AppException):
    """Raised when user is not authorized"""
    def __init__(self, message: str):
        super().__init__(message, status_code=401)


class ForbiddenError(AppException):
    """Raised when user doesn't have permission"""
    def __init__(self, message: str):
        super().__init__(message, status_code=403)


class DatabaseError(AppException):
    """Raised when database operation fails"""
    def __init__(self, message: str):
        super().__init__(message, status_code=500)
