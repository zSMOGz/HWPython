from fastapi import (FastAPI,
                     HTTPException,
                     Request,
                     Path,
                     Form)
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()
templates = Jinja2Templates(directory="templates")

users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int


@app.get("/")
async def get_all_users(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html",
                                      {"request": request,
                                       "users": users})


@app.get("/user/{user_id}")
async def get_user(request: Request,
                   user_id: int) -> HTMLResponse:
    try:
        return templates.TemplateResponse("users.html",
                                          {"request": request,
                                           "user": users[user_id]})
    except IndexError:
        raise HTTPException(status_code=404,
                            detail="User not found")


@app.post("/")
async def create_user(request: Request,
                      username: str = Form(description='Enter username'),
                      age: int = Form()) -> HTMLResponse:
    if users:
        user_id = max(users, key=lambda m: m.id).id + 1
    else:
        user_id = 0
    print(user_id)
    user = User(id=user_id,
                username=username,
                age=age)
    users.append(user)
    try:
        return templates.TemplateResponse("users.html",
                                          {"request": request,
                                           "user": users[user_id]})
    except IndexError:
        raise HTTPException(status_code=404,
                            detail="User not found")

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
        raise HTTPException(status_code=404,
                            detail="User not found")


@app.delete("/user/{user_id}")
async def delete_user(user_id: int = Path(ge=1)) -> User:
    try:
        deleted_user = users.pop(user_id)
        return deleted_user
    except IndexError:
        raise HTTPException(status_code=404,
                            detail="User not found")
