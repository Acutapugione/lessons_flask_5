# %%
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, DeclarativeBase, Mapped, mapped_column


# %%
engine = create_engine("sqlite:///my_db.db", echo=True)

SESSION = sessionmaker(bind=engine, autoflush=True)


# %%
class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)

    # @property
    # @classmethod
    # def __tablename__(cls):
    #     return cls.__name__.lower()


class Animal(Base):
    __tablename__ = "animals"


class User(Base):
    __tablename__ = "users"


# Base.metadata.drop_all(bind=engine)
# Animal.metadata.create_all(bind=engine)
# Base.metadata.create_all(bind=engine)

# %%
session = SESSION()
session.add(User())
session.commit()

# %%
with SESSION.begin() as session:
    session.add(User())
    # session.flush()

    session.add(Animal())
    # session.flush()

    session.add(Animal())
    # session.flush()

    session.add_all({Animal(), Animal(), User()})
