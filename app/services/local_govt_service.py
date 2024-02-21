from sqlalchemy.orm import Session
from app.db import schemas 
from utils import http_exception_404, http_exception_ext_successful, http_except_ext_dict_data
from app.redis_connect.redis import check_redis_item, insert_into_redis
import json
from utils import serialize_localgovt


class Local_Gover_Service:
    
    def __init__(self, db: Session):
        self.db = db
        
    def get_state(self, state_id: int):
        
        redis_key = f"localgovt?state_id={state_id}"
        
        if check_redis_item(redis_key) is not None:
            get_data = check_redis_item(redis_key)
        else:
            
            get_data = self.db.query(schemas.LocalGovt).filter(schemas.LocalGovt.states_id == state_id).all()
            
            if not get_data:
                raise http_exception_404()
            
            serialized_locat_govt_data = [serialize_localgovt(localgovt) for localgovt in get_data]
            local_govt_data_json = json.dumps(serialized_locat_govt_data)
            insert_into_redis(redis_key, local_govt_data_json)
            
            
        response_builder = {
                **http_exception_ext_successful(),
                **http_except_ext_dict_data()
            }
        
        response_builder.update({"data": get_data})
        return response_builder