import os

TEST = True

if TEST:
    FILE_PATH = os.path.abspath(__file__)
    BASE_DIR = os.path.dirname(FILE_PATH)
    DATABASE_FILENAME = 'test_database.db'
    DB_CONNECTION_STRING = f'sqlite+aiosqlite:///{os.path.join(BASE_DIR, DATABASE_FILENAME)}'
else:
    DB_CONNECTION_STRING = ''
