from os import getenv
from pathlib import Path

DB_NAME = 'polytech_db'
DB_USER = getenv('POSTGRES_USER')
DB_PASSWORD = getenv('POSTGRES_PASSWORD')

BASE_DIR = Path(__file__).resolve().parent
DB_INIT_FILE = BASE_DIR / 'mospolytech_db.sql'
CREDENTIALS_FILE = BASE_DIR / 'creds.json'
