from sqlalchemy.orm import Session
from app.db import schemas 
from utils import http_exception_404, http_exception_ext_successful, http_except_ext_dict_data


class Country_Service:
    
    def __init__(self, db: Session):
        self.db = db
        
    def get_all_country(self):
        
        get_data = self.db.query(schemas.Country).all()
        if not get_data:
            raise http_exception_404()
        
        response_builder = {
            **http_exception_ext_successful(),
            **http_except_ext_dict_data()
        }
        
        response_builder.update({"data": get_data})
        return {"detail":response_builder}
        
        
    def get_country(self, continent_id: int):
        
        get_data = self.db.query(schemas.Country).filter(schemas.Country.continent_id == continent_id).first()
        
        if not get_data:
            raise http_exception_404()
        
        response_builder = {
            **http_exception_ext_successful(),
            **http_except_ext_dict_data()
        }
        
        response_builder.update({"data": get_data})
        return {"detail":response_builder}