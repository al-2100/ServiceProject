from peewee import Model, CharField, IntegerField
from src.database import database

class BaseModel(Model):
    class Meta:
        database = database

class User(BaseModel):
    id = IntegerField(primary_key=True)
    name = CharField()
    email = CharField(unique=True)
    password = CharField()
