from pydantic import BaseModel
from datetime import datetime


class Continent(BaseModel):
    id: int
    name: str
    created_at: datetime