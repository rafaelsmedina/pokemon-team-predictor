from sqlalchemy import Column, String, Integer
from app import db

class Ability(db.Model):
    __tablename__ = 'ability'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

    def __iter__(self):
        yield 'id', self.id
        yield 'name', self.name
        yield 'description', self.description