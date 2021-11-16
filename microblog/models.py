from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from core.database import Base
from users.models import User


class Post(Base):
    __tablename__ = "Microblog posts"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String)
    text = Column(String(350))
    date = Column(DateTime)
    user = Column(Integer, ForeignKey(User.id))

    user_id = relationship("User")
