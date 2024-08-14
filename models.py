from sqlalchemy import Boolean,Column, ForeignKey,Integer,String, Text
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50))
    posts = relationship("Post", back_populates="owner")

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50))
    content = Column(String(100))
    user_id = Column(Integer, ForeignKey('users.id'))
    owner = relationship("User", back_populates="posts")
