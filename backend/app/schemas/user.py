from pydantic import BaseModel, EmailStr

#registering
class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str

# for response after registration
class UserResponse(BaseModel):
    id: int
    email: EmailStr
    username: str
    is_active: bool

    class Config:
        from_attributes = True #makes pydantic model work with SQLAlchemy models

# for login response
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None