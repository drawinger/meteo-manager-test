import json
from typing import List

from aiohttp import ClientSession

from environment.config import LB_URL, API_URL, API_KEY, EXTRA_INFO, LAT, LON



async def fetch_meteodata(session: ClientSession, crds: list):
    """
    Получение метеоданных из API
    """

    headers = {
    "lat": crds[0], #61.255977241368896 
    "lon": crds[1], #73.42821764191312
    # "extra": EXTRA_INFO,
    "X-Yandex-API-Key": API_KEY
    }
    print(headers)
    try:
        async with session.get(API_URL, headers = headers) as resp:
            result = await resp.json()
        return result
    except Exception as err:
        print(err) 


async def fetch_meteostations(session: ClientSession) -> List:
    """
    Получение метеостанций
    """
    url = f"{LB_URL}/api/meteoStations"
    filters = {
        "where": {
            "type": "Yandex",
        }
    }
    params = {"filter": json.dumps(filters)}
    async with session.get(url, params = params) as response:
        data = await response.json()
    return data



async def fetch_meteostations_data(session: ClientSession) -> List:
    """
    Получение данных с метеостанций
    """
    url = f"{LB_URL}/api/MeteoStationData"

    async with session.get(url) as response:
        meteostation_data = await response.json()
    return meteostation_data


async def put_meteostations_data(session: ClientSession, meteodata: dict):
    """
    Закладывание данных в лб
    """
    url = f"{LB_URL}/api/MeteoStationData"

    headers = {'Content-Type': 'application/json'}

    async with session.put(url, data=json.dumps(meteodata), headers=headers) as resp:
        if resp.status ==  200:
            print(f'Signal group config succesfully updated for controller')
        else:
            raise Exception(f"Can't update signal group config for controller: [{resp.status} - {resp.reason}]")
