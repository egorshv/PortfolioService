from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from settings import DB_CONNECTION_STRING

Base = declarative_base()


class DBCore:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not DBCore._instance:
            DBCore._instance = super(DBCore, cls).__new__(cls, *args, **kwargs)
        return DBCore._instance

    def __init__(self):
        self.engine = create_async_engine(
            DB_CONNECTION_STRING,
            echo=True,
            future=True,
        )

    async def get_session(self):
        async_session = async_sessionmaker(self.engine, expire_on_commit=False, class_=AsyncSession)

        async with async_session() as session:
            try:
                return session
            finally:
                await session.close()

    async def init_models(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
