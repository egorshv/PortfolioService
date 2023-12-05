import uuid
from typing import Optional, List, Type

from pydantic import BaseModel

from MongoClientSingleton import MongoClientSingleton
from schemas.portfolio import Portfolio
from schemas.state import State
from schemas.trade import Trade
from settings import MONGO_DB_NAME


class BaseDAO:
    def __init__(self, client: MongoClientSingleton, collection_name: str,
                 schema: Type[Portfolio] | Type[State] | Type[Trade]):
        self.client = client
        self.db = self.client.get_database(MONGO_DB_NAME)
        self.collection = self.db.get_collection(collection_name)
        self.schema = schema

    async def _add(self, obj: BaseModel) -> None:
        await self.collection.insert_one(obj)

    async def _get(self, obj_id: uuid.UUID) -> Portfolio | State | Trade:
        obj: BaseModel = await self.collection.find_one(dict(id=obj_id))
        return obj

    async def _delete(self, obj_id: uuid.UUID) -> None:
        await self.collection.delete_one(dict(id=obj_id))

    async def _update(self, obj_id: uuid.UUID, **kwargs) -> Portfolio | State | Trade:
        obj: BaseModel = await self.collection.find_one(dict(id=obj_id))
        for key, value in kwargs.items():
            if hasattr(obj, key):
                setattr(obj, key, value)
        return await self.collection.update_one(dict(id=obj_id), {"$set": obj})

    async def _list(self, **kwargs) -> List[Portfolio | State | Trade]:
        obj_list = list()
        async for obj in self.collection.find(dict(kwargs)):
            obj_list.append(obj)

        return obj_list
