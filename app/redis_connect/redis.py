import redis
from config import config
import json

redis_host = config['redis']['redis_host']
redis_port = config['redis']['redis_port']
r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

    
def insert_into_redis(redis_key:str, redis_date):
    r.set(redis_key, redis_date)

def check_redis_item(key):
    
    value = r.get(key)
    
    if value is not None:
        cached_data = json.loads(value)
        return cached_data
    else:
        return None