from fastapi import APIRouter, Depends, status
from app.services.continent_service import Continent_Service
from app.services.country_service import Country_Service
from app.services.state_service import State_Service
from app.services.local_govt_service import Local_Gover_Service
from app.di.dependencies import continent_service, country_service, state_service, local_govt_service
from app.authentication.oauth2 import  get_current_user


router = APIRouter()


@router.get("/continent", status_code=status.HTTP_200_OK)
async def get_all_continent(is_continent: Continent_Service = Depends(continent_service), injection = Depends(get_current_user)):
    return injection.get_all_continent()

@router.get("/continent/{id}", status_code=status.HTTP_200_OK)
async def get_all_continent(id: int, is_continent: Continent_Service = Depends(continent_service), injection = Depends(get_current_user)):
    return injection.get_continent(id)

@router.get("/country", status_code=status.HTTP_200_OK)
async def get_all_country(is_continent: Country_Service = Depends(country_service), injection = Depends(get_current_user)):
    return injection.get_all_country()

@router.get("/country/{continent_id}", status_code=status.HTTP_200_OK)
async def get_all_country(continent_id: int, is_continent: Country_Service = Depends(country_service), injection = Depends(get_current_user)):
    return injection.get_country(continent_id)

@router.get("/state", status_code=status.HTTP_200_OK)
async def get_all_state(is_state: State_Service = Depends(state_service), injection = Depends(get_current_user)):
    return injection.get_all_state()

@router.get("/state/{country_id}", status_code=status.HTTP_200_OK)
async def get_all_state(country_id: int, is_state: State_Service = Depends(state_service), injection = Depends(get_current_user)):
    return injection.get_state(country_id)

@router.get("/localgovt/{state_id}", status_code=status.HTTP_200_OK)
async def get_all_state(state_id: int, is_local_govt: Local_Gover_Service = Depends(local_govt_service), injection = Depends(get_current_user)):
    return injection.get_state(state_id)


