from sqlalchemy.orm import Session
from app.db import schemas 
from fastapi import  HTTPException


class Continent_Service:
    
    def __init__(self, db: Session):
        self.db = db
        
    def get_continent(self) :
        get_data = self.db.query(schemas.Continent).all()
        if not get_data:
            raise HTTPException(status_code=404, detail={
                    "error": "Resource not found",
                    "message": "The requested resource does not exist on the server."
            })
        else:
            return get_data