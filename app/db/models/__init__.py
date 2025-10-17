# Import models in the correct order to avoid circular imports
# Base models first
from app.db.models.masters.roles import Role
from app.db.models.masters.qualifications import Qualification
from app.db.models.masters.languages import Language

# Then User model
from app.db.models.user import User

# Then models that depend on User
from app.db.models.consultant.consultant_enquiry import ConsultantEnquiry

__all__ = [
    "Role",
    "Qualification", 
    "Language",
    "User",
    "ConsultantEnquiry",
]
