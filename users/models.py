from sqlalchemy import Column, String, Integer, Boolean, DateTime

from core.database import Base


class User(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String(), unique=True)
    email = Column(String(), unique=True)
    password = Column(String())
    date = Column(DateTime)
    is_active = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)
