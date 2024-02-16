from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import app_api
from app.db import database as models 


models.Base.metadata.create_all(bind=models.engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(app_api.router, prefix="/location", tags=["location"])

