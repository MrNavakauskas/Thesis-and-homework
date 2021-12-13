
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///persons.db")
Base = declarative_base()


class Person(Base):
    __tablename__ = "Person"

    id = Column(Integer, primary_key=True)
    name = Column("Name", String)
    surname = Column("Surname", String)
    age = Column("Age", Integer)

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.surname}, {self.age}"


Base.metadata.create_all(engine)
