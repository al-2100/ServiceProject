from peewee import SqliteDatabase

# Configuración de la base de datos SQLite
DATABASE_URL = "product_catalog.db"
database = SqliteDatabase(DATABASE_URL)
