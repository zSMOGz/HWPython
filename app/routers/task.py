from fastapi import APIRouter, Depends, HTTPException, status
from app.models.task import Task
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
    if select(Task).where(Task.username == create_task.username).first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Задача с таким именем уже существует")
    else:
        db.execute(Insert(Task).values(name=create_task.name,
                                       description=create_task.description,
                                       status=create_task.status,
                                       slug=slugify(create_task.name)))
        db.commit()
        return {"status_code": status.HTTP_201_CREATED,
                "message": "Задача успешно создана"}


@router.get("/")
async def get_all_tasks(db: Annotated[Session, Depends(get_db)]):
    tasks = db.query(Task).all()
    return tasks


@router.get("/task_id")
async def get_task_by_id(db: Annotated[Session, Depends(get_db)],
                         task_id: int):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Задача не найдена")
    return task


@router.put("/update")
async def update_task(db: Annotated[Session, Depends(get_db)],
                      task_id: int,
                      update_task: CreateTask):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Задача не найдена")

    db.execute(update(Task).where(Task.id == task_id).values(
        name=update_task.name,
        description=update_task.description,
        status=update_task.status,
        slug=slugify(update_task.name)))

    db.commit()
    return {"status_code": status.HTTP_200_OK,
            "message": "Задача обновлена успешно"}


@router.put("/delete")
async def delete_task(db: Annotated[Session, Depends(get_db)],
                      task_id: int):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Задача не найдена")

    db.execute(update(Task).where(Task.id == task_id).values(
        completed=True))

    db.commit()
    return {"status_code": status.HTTP_200_OK,
            "message": "Задача удалена успешно"}
