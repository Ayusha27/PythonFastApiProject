import uuid

from sqlalchemy import Column, UUID
from sqlalchemy.orm import DeclarativeBase


class Post(DeclarativeBase):
    __tablename__ = "posts"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
