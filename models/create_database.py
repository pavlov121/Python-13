from models.database import Session, create_db
from models.student import Student
from models.group import Group


def create_database(load_faker_data=True):
    create_db()
    if load_faker_data:
        _load_faker_data(Session())


def _load_faker_data(session):
    group1 = Group(group_name='К02-21')
    group2 = Group(group_name='К02Д-21')
    session.add(group1)
    session.add(group2)
    student1 = Student(surname='Павлов', name='Алексей', age=21)
    student2 = Student(surname='Наталья', name='Тимчишина', age=23)
    student3 = Student(surname='Бирюков', name='Артём', age=22)
    student4 = Student(surname='Иванов', name='Иванович', age=25)
    session.add(student1)
    session.add(student2)
    session.add(student3)
    session.add(student4)
    session.commit()
    session.close()
