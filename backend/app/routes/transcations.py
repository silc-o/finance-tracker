from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.transaction import Transaction
from app.schemas.transaction import TransactionCreate, TransactionResponse
from app.dependencies import get_current_user
from app.models.user import User

router = APIRouter(prefix="/transactions", tags=["Transactions"])

#get all transactions for current user
@router.get("/", response_model=List[TransactionResponse])
def get_transactions(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    transactions = db.query(Transaction).filter(Transaction.user_id == current_user.id).all()
    return transactions

@router.post("/", response_model=TransactionResponse)