from fastapi import Depends, HTTPException, status
from typing import Annotated
from sqlalchemy.orm import Session
from app.backend.db_depends import get_db
from app.models.task import Task
from app.models.user import User


async def is_valid_task(db: Annotated[Session, Depends(get_db)],
                        task_id: int):
    try:
        task = db.query(Task).filter(Task.id == task_id).first()
        return task
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Задача не найдена")


async def is_valid_user(db: Annotated[Session, Depends(get_db)],
                        user_id: int):
    try:
        user = db.query(User).filter(User.id == user_id).first()

        return user
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Пользователь не найден")