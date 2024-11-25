from peewee import Model, CharField, ForeignKeyField, IntegerField
from src.database import database
from user_management.src.models import User

class BaseModel(Model):
    class Meta:
        database = database

class Product(BaseModel):
    id = IntegerField(primary_key=True)
    name = CharField()
    description = CharField()
    owner = ForeignKeyField(User, backref="products")
