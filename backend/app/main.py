from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base, engine
from app.models import User, Transaction

# Import routes directly to avoid circular imports
from app.routes.auth import router as auth_router
from app.routes.transactions import router as transactions_router

# Create all database tables automatically on startup
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Allow React frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Finance Tracker API!"}

# Register auth and transactions routes
app.include_router(auth_router)
app.include_router(transactions_router)