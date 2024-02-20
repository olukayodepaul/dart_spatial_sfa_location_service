from fastapi import APIRouter, Depends, status
from app.services.continent_service import Continent_Service
from app.di.dependencies import continent_service
from app.authentication.oauth2 import create_access_token, get_current_user



router = APIRouter()


@router.get("/continent", status_code=status.HTTP_200_OK)
async def get_all_continent(is_continent: Continent_Service = Depends(continent_service), add_route_protection = Depends(get_current_user)):
    return is_continent.get_all_continent()

@router.get("/continent/{id}", status_code=status.HTTP_200_OK)
async def get_all_continent(id: int, is_continent: Continent_Service = Depends(continent_service), add_route_protection = Depends(get_current_user)):
    return is_continent.get_continent(id)

