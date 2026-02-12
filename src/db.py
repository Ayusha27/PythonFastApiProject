import datetime
import uuid
from collections.abc import AsyncGenerator

from sqlalchemy import String
from sqlalchemy import Column, UUID, DateTime
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

DATABASE_URL = "sqlite+aiosqlite///./posts.db"

class Post(DeclarativeBase):
    __tablename__ = "posts"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    caption = Column(String, nullable=False)
    url = Column(String, nullable=False)
    file_name = Column(String, nullable=False)
    file_type = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)

engine = create_async_engine(DATABASE_URL)
async_session = async_sessionmaker(engine, expire_on_commit=False)

#we are creating all the databases and tables here
# it starts a database engine and creates all the tables
async def create_db_tables():
    async with engine.begin() as conn:
        await conn.run_sync(DeclarativeBase.metadata.create_all)

#this get async session will help us to get the session which will allow us to
# access the database and read and write from it asynchronously.
async def get_async_session()-> AsyncGenerator[DeclarativeBase, None]:
    async with async_sessionmaker() as session:
        yield session

