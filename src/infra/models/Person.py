from sqlalchemy import Column, String, UUID
from ..db import Base


class Person(Base):
    __tablename__ = "persons"

    id = Column(UUID, primary_key=True, index=True)
    nickname = Column(String, index=True)
    name = Column(String)
    birthday = Column(String)
    stack = Column(String)
