from typing import List

from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel

app = FastAPI()

users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int


@app.get("/users")
async def get_all_users() -> List[User]:
    return users


@app.post("/user/{username}/{age}")
async def create_user(username: str = Path(description='Enter username',
                                           examples=['SMOG']),
                      age: int = Path(ge=1,
                                      le=200,
                                      description='Enter age',
                                      examples=[18])) -> User:
    user = User(id=len(users) + 1,
                username=username,
                age=age)
    users.append(user)
    return user


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: int = Path(ge=1),
                      username: str = Path(description='Enter username',
                                           examples=['SMOG']),
                      age: int = Path(ge=1,
                                      le=200,
                                      description='Enter age',
                                      examples=[18])) -> User:
    try:
        users[user_id].username = username
        users[user_id].age = age
        return users[user_id]
    except IndexError:
        raise HTTPException(status_code=404, detail="Message not found")


@app.delete("/user/{user_id}")
async def delete_user(user_id: int = Path(ge=1)) -> User:
    try:
        deleted_user = users.pop(user_id)
        return deleted_user
    except IndexError:
        raise HTTPException(status_code=404, detail="Message not found")
