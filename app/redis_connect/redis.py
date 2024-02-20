
import redis
from config import config

def get_redis_connection():
    
    redis_host = config['redis']['redis_host']
    redis_port = config['redis']['redis_port']
    instantiate_redis = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)
    return instantiate_redis