import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='.env')

class Config:
    ENVIRONMENT = os.getenv('FLASK_ENV')
    DATA_BASE_URI=os.getenv('DATA_BASE_URI')
    REDIS_BROKER_BASE_URL = os.getenv('REDIS_BROKER_BASE_URL')