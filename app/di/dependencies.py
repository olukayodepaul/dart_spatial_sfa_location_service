from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.services.continent_service import Continent_Service
from app.services.country_service import Country_Service
from app.services.state_service import State_Service
from app.services.local_govt_service import Local_Govt_Service
from app.authentication.oauth2 import  get_current_user


def continent_service(db: Session = Depends(get_db), payload = Depends(get_current_user)):
    return Continent_Service(db=db, payload = payload)

def country_service(db: Session = Depends(get_db), payload = Depends(get_current_user)):
    return Country_Service(db=db, payload = payload)

def state_service(db: Session = Depends(get_db), payload = Depends(get_current_user)):
    return State_Service(db=db, payload=payload)

def local_govt_service(db: Session = Depends(get_db), payload = Depends(get_current_user)):
    return Local_Govt_Service(db=db, payload=payload)