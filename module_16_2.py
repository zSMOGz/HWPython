from typing import Annotated

from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/")
async def main() -> dict:
    return {"message": "Главная страница"}


@app.get("/user/{user_id}")
async def user(user_id: Annotated[int, Path(ge=1,
                                            le=100,
                                            description='Enter User ID',
                                            examples=[1])]) -> dict:
    return {"message": f"Вы вошли как пользователь № {user_id}"}


@app.get("/user/admin")
async def admin() -> dict:
    return {"message": "Вы вошли как администратор"}


@app.get("/user/{user_name}/{age}")
async def id_paginator(user_name: str = Path(description='Enter username',
                                             examples=['SMOG']),
                       age: int = Path(ge=1,
                                       le=200,
                                       description='Enter age',
                                       examples=[29])) -> dict:
    return {"message": f"Информация о пользователе. Имя: {user_name}, Возраст: {age}"}