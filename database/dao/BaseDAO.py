from typing import List, Optional, Type

from pydantic import BaseModel
from sqlalchemy import select, delete

from database.DBCore import Base


class BaseDAO:
    def __init__(self, session, model: Type[Base], schema: Type[BaseModel]):
        self.schema = schema
        self.session = session
        self.model = model

    async def _create(self, obj: BaseModel) -> BaseModel:
        async with self.session.begin():
            model = self.model(**obj.model_dump())
            self.session.add(model)
            await self.session.commit()
            return self.schema(**model.__dict__)

    async def _get(self, obj_id: int) -> Optional[BaseModel]:
        async with self.session.begin():
            result = await self.session.execute(
                select(self.model).where(self.model.id == obj_id)
            )
            model = result.scalars().first()
            if model is not None:
                return self.schema(**model.__dict__)

    async def _delete(self, obj_id: int) -> None:
        async with self.session.begin():
            try:
                await self.session.execute(
                    delete(self.model).where(self.model.id == obj_id)
                )
                await self.session.commit()
            except Exception as err:
                await self.session.rollback()
                raise err

    async def _delete_all(self) -> None:
        async with self.session.begin():
            try:
                await self.session.execute(
                    delete(self.model)
                )
                await self.session.commit()
            except Exception as err:
                await self.session.rollback()
                raise err

    async def _update(self, obj_id: int, **kwargs) -> Optional[BaseModel]:
        async with self.session.begin():
            q = await self.session.execute(
                select(self.model).where(self.model.id == obj_id)
            )
            model = q.scalars().first()
            for key, value in kwargs.items():
                if hasattr(model, key):
                    setattr(model, key, value)
            if model is not None:
                try:
                    await self.session.commit()
                except Exception as err:
                    await self.session.rollback()
                    raise err
                return self.schema(**model.__dict__)

    async def _list(self, **kwargs) -> Optional[List[BaseModel]]:
        async with self.session.begin():
            q = select(self.model).filter_by(**kwargs)
            result = await self.session.execute(q)
            result = result.scalars().all()
            return [self.schema(**model.__dict__) for model in result]
