from os import getenv
from pathlib import Path


TELEGRAM_BOT_TOKEN = getenv('TELEGRAM_BOT_TOKEN')
DB_NAME = getenv('POSTGRES_DATABASE')
DB_USER = getenv('POSTGRES_USER')
DB_PASSWORD = getenv('POSTGRES_PASSWORD')

BASE_DIR = Path(__file__).resolve().parent
DB_INIT_FILE = BASE_DIR / 'db_schema.sql'
DB_DATA_FILE = BASE_DIR / 'db_data.sql'
