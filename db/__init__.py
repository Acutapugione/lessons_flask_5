from .config import Config


from .models import Group, Student


def migrate():
    with Config.SESSION() as session:
        for i in range(10):
            session.add(Student(name=f"Vasya{i+1}"))
        session.commit()


# migrate()
