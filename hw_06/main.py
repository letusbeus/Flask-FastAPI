import os
from datetime import datetime
from random import random, choice
from typing import List

import sqlalchemy
from databases import Database
from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from hw_06.model import User, UserInput, Item, ItemInput, Order, OrderInput


# Создаем URL-адрес для базы данных
DATABASE_URL = f"sqlite:///{os.path.dirname(os.path.abspath(__file__))}/mydatabase.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
database = Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    "users", metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50)),
    Column("last_name", String(50)),
    Column("email", String(50)),
    Column("password", String(64)),
)

items = sqlalchemy.Table(
    "items", metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50)),
    Column("description", String(150)),
    Column("price", Float),
)

orders = sqlalchemy.Table(
    "orders", metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey('users.id'), nullable=False),
    Column("item_id", Integer, ForeignKey('orders.id'), nullable=False),
    Column("order_date", String(10)),
    Column("status", String(30)),
)

metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get('/')
async def hello_world():
    return {'message': "Welcome!"}


@app.get('/create_fake_items/')
async def create_fake_items():
    for i in range(30):
        query = items.insert().values(name=f"item{i + 1}",
                                      description=f"description{i + 1}",
                                      price=f"{round(1000 * random(), 2):2f}",
                                      )
        await database.execute(query)
    return {'message': 'OK'}


@app.get("/get_items/", response_model=List[Item])
async def read_items():
    query = items.select()
    return await database.fetch_all(query)


@app.get('/get_item/{item_id}', response_model=Item)
async def get_item(item_id: int):
    query = items.select().where(items.c.id == item_id)
    return await database.fetch_one(query)


@app.post('/create_item/', response_model=Item)
async def create_item(item: ItemInput):
    query = items.insert().values(name=item.name,
                                  description=item.description,
                                  price=item.price)
    last_record_id = await database.execute(query)
    return {**item.model_dump(), "id": last_record_id}


@app.put('/update_item/{item_id}', response_model=Item)
async def update_item(item_id: int, new_item: ItemInput):
    query = items.update().where(items.c.id == item_id).values(**new_item.model_dump())
    await database.execute(query)
    return {**new_item.model_dump(), "id": item_id}


@app.delete('/delete_item/{item_id}')
async def delete_item(item_id: int):
    query = items.delete().where(items.c.id == item_id)
    await database.execute(query)
    return {'message': 'Item deleted'}


@app.get('/create_fake_users/')
async def create_fake_users():
    for i in range(10):
        query = users.insert().values(name=f"user{i + 1}",
                                      last_name=f"last_name{i + 1}",
                                      email=f"email{i + 1}@email.com",
                                      password=f"password{i + 1}",
                                      )
        await database.execute(query)
    return {'message': 'OK'}


@app.get("/get_users/", response_model=List[User])
async def read_users():
    query = users.select()
    return await database.fetch_all(query)


@app.get('/get_user/{user_id}', response_model=User)
async def get_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    return await database.fetch_one(query)


@app.post('/create_user/', response_model=User)
async def create_user(user: UserInput):
    query = users.insert().values(name=user.name,
                                  last_name=user.last_name,
                                  email=user.email,
                                  password=user.password)
    last_record_id = await database.execute(query)
    return {**user.model_dump(), "id": last_record_id}


@app.put('/update_user/{user_id}', response_model=User)
async def update_user(user_id: int, new_user: UserInput):
    query = users.update().where(users.c.id == user_id).values(**new_user.model_dump())
    await database.execute(query)
    return {**new_user.model_dump(), "id": user_id}


@app.delete('/delete_user/{user_id}')
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return {'message': 'User deleted'}


@app.get('/generate_fake_orders/')
async def generate_fake_orders():
    existing_users = await database.fetch_all(users.select())
    existing_items = await database.fetch_all(items.select())
    for i in range(20):
        user = choice(existing_users)
        item = choice(existing_items)
        # для разнообразия генерации времени заказа
        # await asyncio.sleep(10 * random())
        query = orders.insert().values(user_id=user['id'],
                                       item_id=item['id'],
                                       order_date=datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
                                       status='Not initiated', )
        await database.execute(query)
    return {'message': 'OK'}


@app.get("/get_orders/", response_model=List[Order])
async def get_orders():
    query = orders.select()
    return await database.fetch_all(query)


@app.get('/get_order/{order_id}', response_model=Order)
async def get_order(order_id: int):
    query = orders.select().where(orders.c.id == order_id)
    return await database.fetch_one(query)


@app.post('/create_order/', response_model=Order)
async def create_order(order: OrderInput):
    query = orders.insert().values(user_id=order.user_id,
                                   item_id=order.item_id,
                                   order_date=order.order_date,
                                   status=order.status)
    last_record_id = await database.execute(query)
    return {**order.model_dump(), "id": last_record_id}


@app.put('/update_order/{order_id}', response_model=Order)
async def update_order(order_id: int, new_order: OrderInput):
    query = orders.update().where(orders.c.id == order_id).values(**new_order.model_dump())
    await database.execute(query)
    return {**new_order.model_dump(), "id": order_id}


@app.delete('/delete_order/{order_id}')
async def delete_order(order_id: int):
    query = orders.delete().where(orders.c.id == order_id)
    await database.execute(query)
    return {'message': 'Order deleted'}
