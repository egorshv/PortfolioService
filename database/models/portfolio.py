from sqlalchemy import Column, Integer, String, Float

from database.DBCore import Base


class Portfolio(Base):
    __tablename__ = 'portfolio'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    last_precision = Column(Float)
    last_recall = Column(Float)
    user_id = Column(Integer, nullable=False)

    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def __repr__(self):
        return f'ID: {self.user_id} Name: {self.name}'
