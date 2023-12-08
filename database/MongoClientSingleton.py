from motor import motor_asyncio


class MongoClientSingleton(motor_asyncio.AsyncIOMotorClient):
    def __init__(self, host, port):
        super().__init__(host, port)

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(MongoClientSingleton, cls).__new__(cls)
        return cls.instance
