from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {
    '1': 'Имя: Anton, Возраст: 24'
}

@app.get('/users')
async def get() -> dict:
    return users

@app.post('/user/{username}/{age}')
async def post(username: Annotated[str, Path(ge=4, le=15, description='Enter your username', example='Andrey')],
               age: int) -> str:
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = f"Имя: {username}, Возраст: {age}"
    return f'User {user_id} is registered'

@app.put('/user/{user_id}/{username}/{age}')
async def put(username: str, age: Annotated[int, Path(ge=1, le=100, description='Enter your age', example='24')],
              user_id: int=Path(ge=1, le=20, description='Enter user_id', example='2')) -> str:
    users[user_id] = f"Имя: {username}, Возраст: {age}"
    return f"The user {user_id} is updated"

@app.delete('/user/{user_id}')
async def delete(user_id) -> str:
    users.pop(user_id)
    return f"The user {user_id} is deleted"
