from database import SessionLocal
from sqlalchemy import func
import crud

db = SessionLocal()

user = crud.create_user(db, "test_user", "test@example.com")
print("Created User:", user.username)

post1 = crud.create_post(db, user.id, "Birinchi Post", "Bu birinchi post")
post2 = crud.create_post(db, user.id, "Ikkinchi Post", "Bu ikkinchi post")
print("Created Posts:", post1.title, ",", post2.title)

posts = crud.get_user_posts(db, user.id)
print("User posts:", posts)

comment1 = crud.create_comment(db, user.id, post1.id, "Zo'r post ekan!")
comment2 = crud.create_comment(db, user.id, post1.id, "Yaxshi yozilgan")
print("Created Comments:", comment1.text, ",", comment2.text)

posts = crud.get_user_posts(db, user.id)
print("User posts:", [p.title for p in posts])

count = crud.get_post_comment_count(db, post1.id)
print(f"Comment'{post1.title}':", count)


latest_posts = crud.get_latest_posts(db, limit=5)
print("Posts:", [p.title for p in latest_posts])


search_results = crud.search_posts_by_title(db, "Birinchi")
print("Results:", [p.title for p in search_results])


page1 = crud.paginate_posts(db, page=1, per_page=1)
print("Page 1:", [p.title for p in page1])

page2 = crud.paginate_posts(db, page=2, per_page=1)
print("Page 2:", [p.title for p in page2])
