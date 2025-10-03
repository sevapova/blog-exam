from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base

# column larni yarating
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, nullable=True)
    created_at = Column(DateTime)

    posts = relationship("Post", back_populates="user")
    comments = relationship("Comment", back_populates="user")

# column larni yarating
class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(256), unique=True, nullable=False)
    body = Column(Text, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime)
    
    user = relationship("User", back_populates="posts")
    comments = relationship("Comment", back_populates="post")

# column larni yarating
class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text, nullable=False)
    post_id = Column(Integer, ForeignKey("posts.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime)    
  
    user = relationship("User", back_populates="comments")
    post = relationship("Post", back_populates="comments")


    
