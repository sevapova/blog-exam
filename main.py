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

        users_data = data.get("users", [])
        users = []
        for item in users_data:
            user = User(
                username=item["username"],
                email=item["email"]
            )
            users.append(user)

        db.add_all(users)
        db.commit()

def insert_posts():
    with SessionLocal() as db:
        with open("demo_data.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        posts_data = data.get("posts", [])
        posts = []
        for item in posts_data:
            post = Post(
                title=item["title"],
                body=item["body"],
                user_id=item["user_id"]
            )
            posts.append(post)

        db.add_all(posts)
        db.commit()

def insert_comments():
    with SessionLocal() as db:
        with open("demo_data.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        comments_data = data.get("comments", [])
        comments = []
        for item in comments_data:
            comment = Comment(
                text=item["text"],
                user_id=item["user_id"],
                post_id=item["post_id"]
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
