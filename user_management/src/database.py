from peewee import SqliteDatabase

DATABASE_URL = "users.db"
database = SqliteDatabase(DATABASE_URL)
