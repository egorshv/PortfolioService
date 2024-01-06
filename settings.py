import os
from dotenv import load_dotenv

TEST = False

if TEST:
    FILE_PATH = os.path.abspath(__file__)
    BASE_DIR = os.path.dirname(FILE_PATH)
    DATABASE_FILENAME = 'test_database.db'
    DB_CONNECTION_STRING = f'sqlite+aiosqlite:///{os.path.join(BASE_DIR, DATABASE_FILENAME)}'
else:
    load_dotenv()
    PASSWORD = os.environ.get('POSTGRES_PASSWORD')
    USER = os.environ.get('POSTGRES_USER')
    HOST = os.environ.get('POSTGRES_HOST')
    PORT = os.environ.get('POSTGRES_PORT')
    DB_NAME = os.environ.get('POSTGRES_NAME')
    DB_CONNECTION_STRING = f'postgresql+asyncpg://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}'
