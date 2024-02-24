from sqlalchemy.orm import Session
from app.db import schemas 
from utils import http_exception_404, http_exception_ext_successful, http_except_ext_dict_data
from typing import Dict

class State_Service:
    
    def __init__(self, db: Session, payload: Dict):
        self.db = db
        
    def all_state(self):
        
        get_data = self.db.query(schemas.State).all()
        if not get_data:
            raise http_exception_404(message="State not found")
        
        response_builder = {
            **http_exception_ext_successful(message="State found"),
            **http_except_ext_dict_data()
        }
        
        response_builder.update({"data": get_data})
        return {"detail":response_builder}
        
        
    def first_state(self, country_id: int):
        
        get_data = self.db.query(schemas.State).filter(schemas.State.country_id == country_id).all()
        
        if not get_data:
            raise http_exception_404(message="State not found")
        
        response_builder = {
            **http_exception_ext_successful(message="State found"),
            **http_except_ext_dict_data()
        }
        
        response_builder.update({"data": get_data})
        return {"detail":response_builder}