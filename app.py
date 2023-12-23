from fastapi import FastAPI
from routes.portfolio import portfolio_router
from database.DBCore import DBCore

app = FastAPI()

app.include_router(portfolio_router)


@app.on_event('startup')
async def startup():
    core = DBCore()
    await core.init_models()
