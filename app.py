from fastapi import FastAPI
from database.MongoClientSingleton import MongoClientSingleton
from routes.portfolio import portfolio_router
from settings import MONGO_DB

app = FastAPI()

app.include_router(portfolio_router)

client = MongoClientSingleton(MONGO_DB['HOST'], MONGO_DB['PORT'])
