from enum import Enum


class UserRole(str, Enum):

    OWNER = "OWNER"

    ADMIN = "ADMIN"

    ANALYST = "ANALYST"

    VIEWER = "VIEWER"