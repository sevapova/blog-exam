from sqlalchemy.orm import Session
from models import User, Post, Comment

# CRUD
def create_user(db: Session, username: str, email: str):
    new = User(username=username, email=email)
    db.add(new)
    db.commit()
    db.refresh(new)
    return new

def create_post(db: Session, user_id: int, title: str, body: str):
    new = Post(user_id=user_id, title=title, body=body)
    db.add(new)
    db.commit()
    db.refresh(new)
    return new

def create_comment(db: Session, user_id: int, post_id: int, text: str):
    new = Comment(user_id=user_id,post_id=post_id, text=text )
    db.add(new)
    db.commit()
    db.refresh(new)
    return new

def update_post(db: Session, post_id: int, title: str, body: str):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        return None
    post.title = title
    post.body = body
    db.commit()
    db.refresh(post)
    return post

def delete_post(db: Session, post_id: int):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        return False
    db.delete(post)
    db.commit()
    return True

# Queries
def get_user_posts(db: Session, user_id: int):
    return db.query(Post).filter(Post.user_id == user_id).all()

def get_post_comment_count(db: Session, post_id: int):
    return db.query(Comment).count(Comment.post_id == post_id).all()

def get_latest_posts(db: Session, limit: int = 5):
    return db.query(Post).order_by(Post.created_at.desc()).limit(limit).all()


def search_posts_by_title(db: Session, keyword: str):
    return db.query(Post).filter(Post.title.ilike(f"%{keyword}%")).all()


def paginate_posts(db: Session, page: int = 1, per_page: int = 5):
    return (
        db.query(Post)
        .order_by(Post.created_at.desc())
        .offset((page - 1) * per_page)
        .limit(per_page)
        .all()
    )
