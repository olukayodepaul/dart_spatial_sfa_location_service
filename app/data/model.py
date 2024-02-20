from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class Continent(BaseModel):
    id: int
    name: str
    created_at: datetime
    
class Employee(BaseModel):
    username: str
    email: EmailStr
    password: str
    
class Token(BaseModel):
    access_token: str
    token_type: str

    
