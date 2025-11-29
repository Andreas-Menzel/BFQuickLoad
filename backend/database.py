from sqlmodel import create_engine, SQLModel

from config import config

DATABASE_URL = f"sqlite:///{config['database']['filename']}"

engine = create_engine(DATABASE_URL, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
