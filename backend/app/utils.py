# * utils is for helper functions that we will be using in our application, such as hashing passwords and creating JWT tokens
from passlib.context import CryptContext
# * handles hashing
from jose import JWTError, jwt
# * handles creating and decoding JWT tokens
from datetime import datetime, timedelta
from app.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# * bcrypt is a hashing algorithm that is used to hash passwords, 
# * it is a one-way hashing algorithm, which means that it cannot be reversed,
# * and it is also a slow hashing algorithm, which makes it more secure against brute-force attacks.
# * deprecated="auto" means that it will automatically detect if the hashing algorithm is deprecated and will use the new one,
# * in this case, it will use bcrypt if the old one is deprecated.

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data:dict) -> str:
    to_encode = data.copy() 
    # * copies the data dict to avoid modifying the original, usually the username
    expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            return None
        return username
    except JWTError:
        return None