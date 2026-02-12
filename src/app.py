from tokenize import String

from fastapi import FastAPI, HTTPException
from src.schemas import TextPost

app = FastAPI()

posts = {}
text_posts = {
    1: {
        "id": 101,
        "author": "Nayak",
        "score": 25,
        "status": "published"
    },
    2: {
        "id": 102,
        "author": "Mohanty",
        "score": 25,
        "status": "draft"
    },
    3: {
        "id": 103,
        "author": "Sharma",
        "score": 42,
        "status": "published"
    },
    4: {
        "id": 104,
        "author": "Das",
        "score": 18,
        "status": "archived"
    },
    5: {
        "id": 105,
        "author": "Patel",
        "score": 88,
        "status": "published"
    }
}
@app.get("/ayusha")
def ayusha():
    return {
        "name" : "Ayusha",
    }

@app.post("/posts")
def posts():
    return posts

@app.post("/postsWithTitle/{title}")
def postsWithTitle(id: int):
    if id not in  text_posts:
        raise HTTPException(status_code=404, detail="Title not found")
    return text_posts[id]


@app.get("/getAllPosts")
def getAllPosts(limit: int= None):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts[id]


@app.post("/posts/create")
def create_post(post: TextPost):
    new_id = max(text_posts.keys()) + 1
    text_posts[new_id] = post
    return text_posts[new_id]