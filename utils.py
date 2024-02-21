from fastapi import  HTTPException, status
import bcrypt
from typing import Dict


def http_exception_404() -> HTTPException:
    http_exception = HTTPException(
        status_code= status.HTTP_404_NOT_FOUND, 
        detail= {
            **http_exception_ext_error(),
            **http_except_ext_dict_data()
            }
        )
    return http_exception

def http_exception_401() -> HTTPException:
    http_exception = HTTPException(
        status_code= status.HTTP_401_UNAUTHORIZED,
        detail= {
            **http_exception_ext()
            },
        headers={
            "WWW-Authenticate": "Bearer"
        }   
        )
    return http_exception


def http_exception_ext_error() -> Dict:
    return {
        "message": "Item Not Found",
        "status": "error",
    }
    
def http_exception_ext() -> Dict:
    return {
        "message": "Validation",
        "status": "error",
    }
    
def http_exception_ext_successful() -> Dict:
    return {
        "message": "Item Found",
        "status": "Successful",
    }
    
def http_except_ext_dict_data() -> Dict:
    return {
        "data" : []
    }
    
def serialize_localgovt(localgovt) :
    return {
        "id": localgovt.id,
        "name": localgovt.name,
        "created_at": localgovt.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f"),
        "states_id": localgovt.states_id
    }



def hash_password(password: str)->bytes:
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

def check_password(plain_password: str, hashed_password: bytes) -> bool:
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password)


    
