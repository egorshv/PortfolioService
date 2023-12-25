from fastapi import FastAPI

from database.DBCore import DBCore
from routes.portfolio import portfolio_router

app = FastAPI()

app.include_router(portfolio_router)


@app.on_event('startup')
async def startup():
    core = DBCore()
    await core.init_models()
