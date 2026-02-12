from pydantic import BaseModel

class TextPost(BaseModel):
    id: int
    author: str
    score: int
    status: str