from jose import jwt, JWTError
import os
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from utils import http_exception_401

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = os.getenv("JWT_SECRET_KEY")
ALGORITHM = os.getenv("JWT_ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("JWT_ACCESS_TOKEN_EXPIRE_MINUTES"))

def create_access_token(payload: dict):
    to_encode = payload.copy()
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)
    return encoded_jwt


def verify_access_token(token: str, credential_exception):
    
    try:
        pay_load = jwt.decode(token, SECRET_KEY, ALGORITHM)
        username:str = pay_load.get("username")
        
        if id is None:
            raise credential_exception
        token_date = { "username": username }
    except JWTError:
        raise credential_exception
    
    return token_date

def get_current_user(token: str = Depends(oauth2_scheme)):
    credential_exception = http_exception_401()
    return verify_access_token(token, credential_exception)