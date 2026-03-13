from pydantic import BaseModel
from datetime import datetime
from app.models.transaction import TransactionType  

class TransactionCreate(BaseModel):
    amount: float
    description: str | None = None
    date: datetime
    type: TransactionType

class TransactionResponse(BaseModel):
    id: int
    amount: float
    description: str | None = None
    category: str
    date: datetime
    type: TransactionType
    user_id: int

    class Config:
        from_attributes = True #makes pydantic model work with SQLAlchemy models