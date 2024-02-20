from sqlalchemy.orm import Session
from app.db import schemas 
# from utils import http_exception
from app.data.model import Employee
from app.authentication.oauth2 import create_access_token

class Country_Service:
    
    def __init__(self, db: Session):
        self.db = db
    
    def get_all_country(self):
        
        get_data = self.db.query(schemas.Country).all()
        # if not get_data:
        #     raise http_exception(message="Not country set")
        # else:
        #     return get_data
        return {}
        
    def get_filtered_country(self, user_credential: Employee):
        
        user = self.db.query(schemas.Country).filter(schemas.Country.name == user_credential.username).first()
        
        # if not user:
        #     raise http_exception(
        #         message="Invalid credentials"
        #     )
            
        # if not user_credential.username == 'Nigeria':
        #     raise http_exception(
        #         message="Invalid credentials"
        #  )
        
        return {}


        # get_data = self.db.query(schemas.Country).filter(schemas.Country.continent_id == continentid).first()
        # if not get_data:
        #     raise HTTPException()
        # else:
        #     return get_data