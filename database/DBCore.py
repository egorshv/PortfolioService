from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from database.models.base import Base
from settings import DB_CONNECTION_STRING


class DBCore:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not DBCore._instance:
            DBCore._instance = super(DBCore, cls).__new__(cls, *args, **kwargs)
        return DBCore._instance

    def __init__(self):
        self.engine = create_async_engine(
            DB_CONNECTION_STRING,
            echo=True
        )

    async def get_session(self):
        async_session = async_sessionmaker(self.engine, expire_on_commit=False)

        async with async_session() as session:
            try:
                return session
            finally:
                await session.close()

    async def init_models(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    async def close_connection(self):
        await self.engine.dispose()
