from fastapi import APIRouter, Depends, status, HTTPException
from typing import List
from app.services.continent_service import Continent_Service
from app.services.country_service import Country_Service
from app.di.dependencies import continent_service
from app.di.dependencies import country_service

router = APIRouter()


@router.get("/continent", status_code=status.HTTP_200_OK)
async def get_all_continent(is_continent: Continent_Service = Depends(continent_service)):
    return is_continent.get_continent()


@router.get("/country", status_code=status.HTTP_200_OK)
def get_all_country(is_country: Country_Service = Depends(country_service)):
    return is_country.get_all_country()

@router.get("/country/{continentid}", status_code=status.HTTP_200_OK)
def get_filtered_country(continentid : int, is_country: Country_Service = Depends(country_service)):
    return is_country.get_filtered_country(continentid)

# @router.get("/state", status_code=status.HTTP_200_OK)
# def get_all_state():
#     return {}

# @router.get("/state/{id}", status_code=status.HTTP_200_OK)
# def get_filtered_state(id: int):
#     return {}

# @router.get("/localgovt", status_code=status.HTTP_200_OK)
# def get_all_local_govt():
#     return {}

# @router.get("/localgovt/{id}", status_code=status.HTTP_200_OK)
# def get_filtered_local_govt(id : int):
#     return {}




# #  keep the response model for now
# @router.post("/opening/", response_model=List[OpenAcc], status_code= status.HTTP_201_CREATED, )
# def open_account(customer_acc: OpenAcc, acc: AccountOpeningService = Depends(open_account)):
#     return acc.open_accounts(customer_acc)
