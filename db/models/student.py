from sqlalchemy.orm import Mapped, mapped_column

# from sqlalchemy import ForeignKey, String, Integer
from . import Config


class Student(Config.BASE):
    __tablename__ = "students"

    name: Mapped[str]
