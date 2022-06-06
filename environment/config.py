import os
import yaml
from pathlib import Path

CUR_DIR = Path(__file__).resolve().parent
DEFAULT_CONFIG_DIR = CUR_DIR / 'config.default.yaml'


try:
    # logger.info("Reading config file from /etc/meteo-api/config.yml")
    with open("/etc/meteo-api/config.yml", 'r') as config_file:
        config = yaml.safe_load(config_file)
except Exception as e:
    # logger.warning("No config file detected! Apply default configuration!")
    with open(DEFAULT_CONFIG_DIR, 'r') as config_file:
        config = yaml.safe_load(config_file)


env_keys = os.environ.keys()

if 'LB_URL' in env_keys:
    config['lb_url'] = os.getenv('LB_URL')

if 'API_URL' in env_keys:
    config['api_url'] = os.getenv('API_URL')

if 'API_KEY' in env_keys:
    config['api_key'] = os.getenv('API_KEY')

if 'EXTRA_INFO' in env_keys:
    config['extra'] = os.getenv('EXTRA_INFO')

if 'LAT' in env_keys:
    config['coordinates']['lat'] = os.getenv('LAT') 

if 'LON' in env_keys:
    config['coordinates']['lon'] = os.getenv('LON')   

if 'METEODATA_UPDATE_INTERVAL' in env_keys:
    config['monitoring_intervals']['meteodata'] = int(os.getenv('METEODATA_UPDATE_INTERVAL'))


VERSION = config['version']
DEBUG = config['debug']
PROJECT_NAME = config['project_name']
LOGGING_CONFIG = config['logger']

HOST = config['host']
PORT = config['port']

LB_URL = config['lb_url']

API_URL = config['api_url']
API_KEY = config['api_key']
EXTRA_INFO = config['extra']
LAT = config['coordinates']['lat']
LON = config['coordinates']['lon']

METEODATA_UPDATE_INTERVAL = config['monitoring_intervals']['controllers']

