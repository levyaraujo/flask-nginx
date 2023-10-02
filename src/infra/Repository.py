from .db import sessionFactory as session, Person


class PersonRepository:
    @staticmethod
    def create_person(nickname: str, name: str, birthday: str, stack: list[str]):
        person = Person(nickname=nickname, name=name, birthday=birthday, stack=stack)
        session.add(person)
        session.commit()
        return person

    @staticmethod
    def get_person_by_id(id: str):
        result = session.query(Person).filter_by(id=id).first()
        return result

    @staticmethod
    def person_exists(nickname: str):
        result = session.query(Person).filter_by(nickname=nickname).first()
        return result

    @staticmethod
    def update_person(person: Person, name: str, birthday: str, stack: list[str]):
        person.name = name
        person.birthday = birthday
        person.stack = stack
        person.stack = stack
        session.commit()
        return person

    @staticmethod
    def delete_person(person: Person):
        session.delete(person)
        session.commit()
