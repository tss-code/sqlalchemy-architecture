import os
from dotenv import dotenv_values

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
ENV_PATH = os.path.join(BASE_DIR, '../.env')

def load_env():
    try:
        return { **dotenv_values(ENV_PATH) }
    except Exception as e:
        raise e

CONFIG = load_env()