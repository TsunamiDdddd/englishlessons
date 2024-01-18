from databases import Database
from sqlalchemy import MetaData, create_engine

DATABASE_URL = "postgresql://....@localhost:5432/db"

engine = create_engine(DATABASE_URL)
metadata = MetaData()

database = Database(DATABASE_URL)