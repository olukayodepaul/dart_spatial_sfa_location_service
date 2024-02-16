from sqlalchemy.orm import Session
from app.db import schemas 
from utils import HTTPException

class Country_Service:
    
    def __init__(self, db: Session):
        self.db = db
    
    def get_all_country(self):
        get_data = self.db.query(schemas.Country).all()
        if not get_data:
            raise HTTPException()
        else:
            return get_data
    
    def get_filtered_country(self, continentid: int):
        get_data = self.db.query(schemas.Country).filter(schemas.Country.continent_id == continentid).first()
        if not get_data:
            raise HTTPException()
        else:
            return get_data