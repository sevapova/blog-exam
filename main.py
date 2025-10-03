import json
from database import Base, engine, SessionLocal
from models import User, Post, Comment

def init_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

def load_demo_data():
    with SessionLocal() as db:
        with open("demo_data.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        users = []
        for item in data:
            user = User(
                username=item['username'],
                email=item['email'],
                created_at=item['created_at']
            )
            users.append(user)

        db.add_all(users)
        db.commit()

def insert_posts():
    with SessionLocal() as db:
        with open("demo_data.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        posts = []
        for item in data:
            post = Post(
                title=item['title'],
                body=item['body'],
                user_id=item['user_id'],
                created_at=item['created_at']
            )
            posts.append(post)

        db.add_all(posts)
        db.commit()

def insert_comments():
    with SessionLocal() as db:
        with open("demo_data.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        comments = []
        for item in data:
            comment = Comment(
                text=item['text'],
                post_id=item['post_id'],
                user_id=item['user_id'],
                created_at=item['created_at']
            )
            comments.append(comment)

        db.add_all(comments)
        db.commit()

if __name__ == "__main__":
    init_db()
    load_demo_data()
    insert_posts()
    insert_comments()
    print("✅ Database initialized and demo data loaded!")
