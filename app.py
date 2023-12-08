from fastapi import FastAPI
from database.MongoClientSingleton import MongoClientSingleton
from settings import MONGO_DB

app = FastAPI()

client = MongoClientSingleton(MONGO_DB['HOST'], MONGO_DB['PORT'])
