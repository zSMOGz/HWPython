from fastapi import APIRouter, Depends, HTTPException, status
from typing import Annotated
from sqlalchemy import Insert, update, select, delete
from sqlalchemy.orm import Session
from slugify import slugify  # pip install python-slugify
from app.backend.db_depends import get_db
from app.schemas import CreateUser
from app.models.user import User

router = APIRouter(prefix="/user",
                   tags=["user"])


@router.post("/create")
async def create_user(db: Annotated[Session, Depends(get_db)],
                      create_user: CreateUser):
    if select(User).where(User.username == create_user.username):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Пользователь с таким именем уже существует")
    else:
        db.execute(Insert(User).values(username=create_user.username,
                                       firstname=create_user.firstname,
                                       lastname=create_user.lastname,
                                       age=create_user.age,
                                       slug=slugify(create_user.username)))
        db.commit()
        return {"status_code": status.HTTP_201_CREATED,
                "message": "Пользователь создан"}


@router.get("/")
async def get_all_users(db: Annotated[Session, Depends(get_db)]):
    try:
        users = db.query(User).all()
        return users
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Пользователь не найден")


@router.get("/user_id")
async def get_user_by_id(db: Annotated[Session, Depends(get_db)],
                         user_id: int):
    try:
        user = db.query(User).filter(User.id == user_id).first()

        return user
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Пользователь не найден")


@router.put("/update")
async def update_user(db: Annotated[Session, Depends(get_db)],
                      user_id: int,
                      update_user: CreateUser):
    try:
        user = db.query(User).filter(User.id == user_id).first()
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Пользователь не найден")

    try:
        db.execute(update(User).where(User.id == user_id).values(
            username=update_user.username,
            firstname=update_user.firstname,
            lastname=update_user.lastname,
            age=update_user.age,
            slug=slugify(update_user.username)))

        db.commit()
        return {"status_code": status.HTTP_200_OK,
                "message": "Пользователь обновлен"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_304_NOT_MODIFIED,
                            detail="Ошбика обновления пользователя")


@router.put("/delete")
async def delete_user(db: Annotated[Session, Depends(get_db)],
                      user_id: int):
    try:
        user = db.query(User).filter(User.id == user_id).first()
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Пользователь не найден")
    try:
        db.execute(delete(User).where(User.id == user_id))

        db.commit()
        return {"status_code": status.HTTP_200_OK,
                "message": "Пользователь удален"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_304_NOT_MODIFIED,
                            detail="Ошибка удаления пользователя")
