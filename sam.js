// # from app.services.country_service import Country_Service
// # from app.di.dependencies import country_service
// # from app.data.model import Employee
// # from fastapi.security.oauth2 import OAuth2PasswordRequestForm
// # from app.db.database import get_db
// # from sqlalchemy.orm import Session

// # from datetime import datetime, timedelta, timezone



// # @router.get("/country", status_code=status.HTTP_200_OK)
// # def get_all_country(is_country: Country_Service = Depends(country_service)):
// #     return is_country.get_all_country()

// # @router.get("/country/r", status_code=status.HTTP_200_OK)
// # def get_filtered_country(employee: Employee, is_country: Country_Service = Depends(country_service)):
// #     return is_country.get_filtered_country(employee)

// # Protect User
// # @router.get("/country/q")
// # def get_filtered_country(user_id = Depends(get_current_user)):
// #     print(user_id)
// #     return {}
    
    

// # #Protect User
// # @router.get("/country/m")
// # def get_filtered_country(credential: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    
// #     payload = {
// #         "username": credential.username,
// #         "exp": datetime.now(timezone.utc) + timedelta(hours=60*60*60)
// #     }
    
// #     access_token = create_access_token(payload=payload)
// #     return ({"access_token" : access_token,  "token_type": "bearer"})



// # {
// #     "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoicGF1bCIsImV4cCI6MTcwODE4ODYwOH0.FZ5KhhyfvRZZzz-0B5P-MuXY9B0k6-UktkzewzeMaGU",
// #     "token_type": "bearer"
// # }


// # @router.get("/state", status_code=status.HTTP_200_OK)
// # def get_all_state():
// #     return {}

// # @router.get("/state/{id}", status_code=status.HTTP_200_OK)
// # def get_filtered_state(id: int):
// #     return {}

// # @router.get("/localgovt", status_code=status.HTTP_200_OK)
// # def get_all_local_govt():
// #     return {}

// # @router.get("/localgovt/{id}", status_code=status.HTTP_200_OK)
// # def get_filtered_local_govt(id : int):
// #     return {}




// # #  keep the response model for now
// # @router.post("/opening/", response_model=List[OpenAcc], status_code= status.HTTP_201_CREATED, )
// # def open_account(customer_acc: OpenAcc, acc: AccountOpeningService = Depends(open_account)):
// #     return acc.open_accounts(customer_acc)





from sqlalchemy.orm import Session
from app.db import schemas 
# from utils import http_exception
from app.data.model import Employee
from app.authentication.oauth2 import create_access_token

class Country_Service:
    
    def __init__(self, db: Session):
        self.db = db
    
    def get_all_country(self):
        
        get_data = self.db.query(schemas.Country).all()
        # if not get_data:
        #     raise http_exception(message="Not country set")
        # else:
        #     return get_data
        return {}
        
    def get_filtered_country(self, user_credential: Employee):
        
        user = self.db.query(schemas.Country).filter(schemas.Country.name == user_credential.username).first()
        
        # if not user:
        #     raise http_exception(
        #         message="Invalid credentials"
        #     )
            
        # if not user_credential.username == 'Nigeria':
        #     raise http_exception(
        #         message="Invalid credentials"
        #  )
        
        return {}


        # get_data = self.db.query(schemas.Country).filter(schemas.Country.continent_id == continentid).first()
        # if not get_data:
        #     raise HTTPException()
        # else:
        #     return get_data