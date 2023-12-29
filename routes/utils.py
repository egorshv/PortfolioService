from sqlalchemy.ext.asyncio import AsyncSession

from database.DBCore import DBCore


async def get_async_session() -> AsyncSession:
    return await DBCore().get_session()
