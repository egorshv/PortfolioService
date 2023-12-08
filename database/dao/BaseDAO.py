from typing import List, Optional

from pydantic import BaseModel

from database.MongoClientSingleton import MongoClientSingleton
from settings import MONGO_DB


class BaseDAO:
    def __init__(self, client: MongoClientSingleton, collection_name: str, schema):
        self.client = client
        self.db = self.client.get_database(MONGO_DB['DB_NAME'])
        self.collection = self.db.get_collection(collection_name)
        self.schema = schema

    async def _add(self, obj: BaseModel) -> None:
        await self.collection.insert_one(obj.model_dump())

    async def _get(self, **kwargs) -> Optional[BaseModel]:
        obj: dict = await self.collection.find_one(kwargs)
        model = self.schema(**obj)
        return model

    async def _delete(self, **kwargs) -> None:
        await self.collection.delete_one(kwargs)

    async def _delete_many(self, **kwargs) -> None:
        await self.collection.delete_many(kwargs)

    async def _update(self, obj_to_update_params: dict, **kwargs) -> Optional[BaseModel]:
        obj_to_update_json: dict = await self.collection.find_one(obj_to_update_params)
        obj_to_update: BaseModel = self.schema(**obj_to_update_json)

        for key, value in kwargs.items():
            if hasattr(obj_to_update, key):
                setattr(obj_to_update, key, value)

        await self.collection.update_one(obj_to_update_params, {"$set": obj_to_update.model_dump()})
        return obj_to_update

    async def _list(self, **kwargs) -> Optional[List[BaseModel]]:
        obj_list = list()
        async for obj_json in self.collection.find(dict(kwargs)):
            obj: BaseModel = self.schema(**obj_json)
            obj_list.append(obj)

        return obj_list
