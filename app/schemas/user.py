from pydantic import BaseModel
from pydantic import EmailStr


class UserResponse(BaseModel):

    id: str

    email: EmailStr

    full_name: str

    role: str

    class Config:
        from_attributes = True