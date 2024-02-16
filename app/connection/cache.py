import os
import redis

def get_redis_connection():
    
    redis_host = os.getenv("REDIS_HOST")
    redis_port = int(os.getenv("REDIS_PORT"))
    r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)
    return r