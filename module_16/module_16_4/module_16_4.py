from fastapi import FastAPI, Body, HTTPException, Path
from typing import Annotated, List
from pydantic import BaseModel

app = FastAPI()

users = []

class User(BaseModel):
    id: int
    username: str
    age: int


@app.get('/users')
async def get() -> List[User]:
    return users

@app.post('/user/{username}/{age}')
async def post(username: str, age: int) -> str:
    user_id = len(users) + 1
    user = User(id=user_id, username=username, age=age)
    users.append(user)
    return f'User {username} is registered'

@app.put('/user/{user_id}/{username}/{age}')
async def put(username: str, age: int, user_id: int) -> str:
    try:
        users[user_id - 1].username = username
        users[user_id - 1].age = age
        return f"The user {user_id} is updated"
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")

@app.delete('/user/{user_id}')
async def delete(user_id: int) -> str:
    try:
        users.pop(user_id - 1)
        return f"The user {user_id} is deleted"
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")