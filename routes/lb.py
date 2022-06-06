import aiohttp
from typing import List, Optional
from fastapi import APIRouter

from lib import lb

router = APIRouter()
from environment.config import LAT, LON


@router.get('/get_meteo', tags=['Meteo API'])
async def fetch_meteodata(lat, lon):
    """
    Получение метеоданных из API
    """

    async with aiohttp.ClientSession() as session:
        meteo = await lb.fetch_meteodata(session, [lat,lon])
    return meteo


@router.get('/lb/get_meteostation', tags=['Loopback'])
async def fetch_meteostations():
    """
    Получение данных о метеостанциях из lb
    """
    async with aiohttp.ClientSession() as session:
        meteostations = await lb.fetch_meteostations(session)
    return meteostations


@router.get('/lb/get_meteostation_data', tags=['Loopback'])
async def fetch_meteostations_data():
    """
    Получение метеоданных из lb
    """
    async with aiohttp.ClientSession() as session:
        meteostations_data = await lb.fetch_meteostations_data(session)
    return meteostations_data


@router.post('/lb/set_meteostation_data', tags=['Loopback'])
async def update_meteostations_data():
    """
    Запись метеоданных в lb
    """
    async with aiohttp.ClientSession() as session:
        await lb.put_meteostations_data(session)
    
    
