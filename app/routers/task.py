from fastapi import APIRouter, Depends, HTTPException, status
from app.models.task import Task
from app.routers.validator import *
from sqlalchemy import Insert, select, update
from sqlalchemy.orm import Session
from app.backend.db_depends import get_db
from app.schemas import CreateTask
from typing import Annotated
from slugify import slugify  # pip install python-slugify

router = APIRouter(prefix="/task",
                   tags=["task"])


@router.post("/create")
async def create_task(db: Annotated[Session, Depends(get_db)],
                      create_task: CreateTask):
    try:
        if db.query(Task).filter(Task.title == create_task.title).first():
            raise HTTPException(status_code=status.HTTP_302_FOUND,
                                detail="Задача с таким именем уже существует")

        await is_valid_user(db,
                            create_task.user_id)

        db.execute(Insert(Task).values(title=create_task.title,
                                       content=create_task.content,
                                       priority=create_task.priority,
                                       user_id=create_task.user_id,
                                       slug=slugify(create_task.title)))
        db.commit()
        return {"status_code": status.HTTP_201_CREATED,
                "transaction": "Задача успешно создана"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_304_NOT_MODIFIED,
                            detail="Ошибка при создании задачи")


@router.get("/")
async def get_all_tasks(db: Annotated[Session, Depends(get_db)]):
    try:
        tasks = db.query(Task).where(Task.completed == False).all()
        return tasks
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Задачи не найдены")


@router.get("/task_id")
async def get_task_by_id(db: Annotated[Session, Depends(get_db)],
                         task_id: int):
    task = await is_valid_task(db,
                               task_id)
    return task


@router.get("/user_id/tasks")
async def get_tasks_by_user_id(db: Annotated[Session, Depends(get_db)],
                               user_id: int):
    try:
        tasks = db.query(Task).filter(Task.user_id == user_id).all()
        return tasks
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Задачи данного пользователя не найдены")


@router.put("/update")
async def update_task(db: Annotated[Session, Depends(get_db)],
                      task_id: int,
                      update_task: CreateTask):
    try:
        await is_valid_task(db,
                            task_id)

        db.execute(update(Task).where(Task.id == task_id).values(
            title=update_task.title,
            content=update_task.content,
            priority=update_task.priority,
            user_id=update_task.user_id,
            slug=slugify(update_task.title)))

        db.commit()
        return {"status_code": status.HTTP_200_OK,
                "message": "Задача обновлена успешно"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_304_NOT_MODIFIED,
                            detail="Ошибка обновления задачи")


@router.put("/delete")
async def delete_task(db: Annotated[Session, Depends(get_db)],
                      task_id: int):
    try:
        await is_valid_task(db,
                            task_id)

        db.execute(update(Task).where(Task.id == task_id).values(
            completed=True))

        db.commit()
        return {"status_code": status.HTTP_200_OK,
                "message": "Задача удалена успешно"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_304_NOT_MODIFIED,
                            detail="Ошибка удаления задачи")
