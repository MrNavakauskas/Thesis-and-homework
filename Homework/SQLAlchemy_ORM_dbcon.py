
from SQLAlchemy_ORM_person import Person

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///persons.db')
Session = sessionmaker(bind=engine)
session = Session()


def add_record(name, surname, age):
    person = Person(name, surname, age)
    session.add(person)
    session.commit()


def update_record(record_id, newname, newsurname, newage):
    person = session.query(Person).get(record_id)
    person.name = newname
    person.surname = newsurname
    person.age = newage
    session.commit()


def delete_record(record_id):
    person = session.query(Person).get(record_id)
    session.delete(person)
    session.commit()


def get_all_records_list():
    return session.query(Person).all()
