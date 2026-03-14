from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from app.utils import decode_access_token

# * dependencies for authentication and getting the current user
# * it checks if a user is logged in before letting them access protected routes.

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")
# * token extractor

# * use get_current_user as a dependency in any route that needs authentication, 
# * and it will automatically check the token and return the user if the token is valid.
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
    )

    username = decode_access_token(token)
    if username is None:
        raise credentials_exception
    
    user = db.query(User).filter(User.username == username).first()
    if user is None:
        raise credentials_exception
    
    return user