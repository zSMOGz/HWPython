from app.backend.db import Base
from sqlalchemy import (Column,
                        ForeignKey,
                        Integer,
                        String,
                        Boolean,
                        Float)
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer,
                primary_key=True,
                index=True)
    username = Column(String(100))
    firstname = Column(String(100))
    lastname = Column(String(100))
    age = Column(Integer)
    slug = Column(String,
                  unique=True,
                  index=True)

    tasks = relationship('Task',
                         back_populates='user')


from sqlalchemy.schema import CreateTable

print(CreateTable(User.__table__))
