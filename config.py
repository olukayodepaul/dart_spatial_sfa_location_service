import os
from dotenv import load_dotenv
load_dotenv()

config = dict({
    "redis":{
        "redis_host": os.getenv("REDIS_HOST"),
        "redis_port" : int(os.getenv("REDIS_PORT")),
    },
    "postgresql": {
        "db_user" : os.getenv("DB_USER"),
        "db_password" : os.getenv("DB_PASSWORD"),
        "db_host" : os.getenv("DB_HOST"),
        "db_port" : os.getenv("DB_PORT"),
        "db_name" : os.getenv("DB_NAME")
    },
    "jwt" :{
        "jwt_secret_key": os.getenv("JWT_SECRET_KEY"),
        "algorithm": os.getenv("JWT_ALGORITHM")
    }
})
