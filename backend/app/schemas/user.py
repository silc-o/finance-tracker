from pydantic import BaseModel, EmailStr 
# * base model is used to create a model for the data that we will be receiving and sending
# * must follow the template of the base model, otherwise it will throw an error

# * schema is used to define the structure of the data that we will be receiving and sending
# * it is used to validate the data that we will be receiving and sending

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
        from_attributes = True # * makes pydantic model work with SQLAlchemy models

# for login response
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None