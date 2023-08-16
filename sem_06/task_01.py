"""
Разработать API для управления списком пользователей с
использованием базы данных SQLite. Для этого создайте
модель User со следующими полями:
○ id: int (идентификатор пользователя, генерируется
автоматически)
○ username: str (имя пользователя)
○ email: str (электронная почта пользователя)
○ password: str (пароль пользователя)
"""
from typing import List
from fastapi import FastAPI
from databases import Database
from pydantic import BaseModel, Field
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./mydatabase.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
database = Database(DATABASE_URL)


class User(BaseModel):
    id: int = Field(default=None, alias='user_id')
    username: str = Field(..., title='Name', min_length=2, max_length=50)
    email: str = Field(..., title='Email', min_length=6, max_length=50)
    userpwd: str = Field(..., title='Password', min_length=6, max_length=50)

    class Config:
        orm_mode = True


class DBUser(Base):
    __table__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50))
    email = Column(String(50))
    userpwd = Column(String(50))


Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.on_event('startup')
async def startup():
    await database.connect()


@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/users/", response_model=User)
async def create_user(user: User):
    query = DBUser.table.insert().values(**user.dict())
    user.id = await database.execute(query)
    return user


@app.get('/users/', response_model=List[User])
async def read_users():
    query = DBUser.table.select()
    users = await database.fetch_all(query)
    return [User(**user) for user in users]


# @app.get()
#
# @app.post()
#
# @app.put()
#
# @app.delete()
