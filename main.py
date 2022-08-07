from fastapi import FastAPI
from typing import List
from starlette.middleware.cors import CORSMiddleware
from db import session
from model import User, UserTable

app = FastAPI()

app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_credentials=True,
    allow_methods=["*"], allowheaders=["*"]
)


@app.get("/users")
def read_users():
    users = session.query(UserTable).all()
    return users


@app.get("/users/{user_id")
def read_user(user_id: int):
    user = session.query(UserTable).filter(UserTable.id == user_id).first()
    return user


@app.post("/user")
def create_users(name: str, age: int):
    user = UserTable()
    user.name = name
    user.age = age
    session.add(user)
    session.commit()

    return f"{name} created"


@app.put("/users")
def update_user(users: List[User]):
    for i in users:
        user = session.query(UserTable).filter(UserTable.id == i.id.first())
        user.name = i.name
        user.age = i.age
        session.commit()

    return f"{i.name} updated"


@ app.delete("/users")
def read_users(user_id: int):
    user = session.query(UserTable).filter(UserTable.id == user_id).first()
    session.commit()
    return read_users
