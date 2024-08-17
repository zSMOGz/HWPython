from fastapi import FastAPI, Path

USERNAME_DESCRIPTION = 'Введите имя пользователя'
USER_ID_DESCRIPTION = 'Введите идентификатор пользователя (больше 1)'
AGE_DESCRIPTION = 'Введите возраст (больше 1 и меньше 200)'

app = FastAPI()

users_db = {"1": "Имя: Example, возраст: 18"}


@app.get("/users")
async def get_all_users() -> dict:
    return users_db


@app.post("/user/{username}/{age}")
async def create_user(username: str = Path(description=USERNAME_DESCRIPTION,
                                           examples=['SMOG']),
                      age: int = Path(ge=1,
                                      le=200,
                                      description=AGE_DESCRIPTION,
                                      examples=[18])) -> str:
    current_index = str(int(max(users_db, key=int)) + 1)
    users_db[current_index] = f"Имя: {username}, возраст: {age}"
    return f"Пользователь {current_index} зарегистрирован"


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: str = Path(description=USER_ID_DESCRIPTION,
                                          ge=1),
                      username: str = Path(description=USERNAME_DESCRIPTION,
                                           examples=['SMOG']),
                      age: int = Path(ge=1,
                                      le=200,
                                      description=AGE_DESCRIPTION,
                                      examples=[18])) -> str:
    users_db[user_id] = f"Имя: {username}, возраст: {age}"
    return f"Пользователь {user_id} обновлён"


@app.delete("/user/{user_id}")
async def delete_user(user_id: str = Path(description=USER_ID_DESCRIPTION,
                                          ge=1)) -> str:
    users_db.pop(user_id)
    return f"Пользователь {user_id} был удалён"
