from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, String, Integer


HOST = "db"
PORT = 5432
pool_parameters = {
    "pool_size": 5,
    "max_overflow": 10,
}

DATABASE_URL = f"postgresql://root:root@{HOST}:{PORT}/person_db"  # Fixed the URL format for synchronous

engine = create_engine(DATABASE_URL, echo=True, **pool_parameters)
Session = sessionmaker(bind=engine)
sessionFactory = Session()
Base = declarative_base()


def create_tables():
    Base.metadata.create_all(bind=engine)


class Person(Base):
    __tablename__ = "persons"

    id = Column(Integer, primary_key=True, index=True)
    nickname = Column(String, index=True)
    name = Column(String)
    birthday = Column(String)
    stack = Column(String)
