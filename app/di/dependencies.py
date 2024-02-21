from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.services.continent_service import Continent_Service
from app.services.country_service import Country_Service
from app.services.state_service import State_Service
from app.services.local_govt_service import Local_Gover_Service


def continent_service(db: Session = Depends(get_db)):
    return Continent_Service(db=db)

def country_service(db: Session = Depends(get_db)):
    return Country_Service(db=db)

def state_service(db: Session = Depends(get_db)):
    return State_Service(db=db)

def local_govt_service(db: Session = Depends(get_db)):
    return Local_Gover_Service(db=db)

