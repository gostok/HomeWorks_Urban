from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import Annotated
from sqlalchemy import insert, select, update, delete
from slugify import slugify

from app.bakend.db_depends import get_db
from app.models import *
from app.schemas import CreateTask, UpdateTask

router = APIRouter(prefix='/task', tags=['task'])

@router.get('/')
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    tasks = db.scalars(select(Task)).all()
    return tasks

@router.get('/task_id')
async def task_by_id(db: Annotated[Session, Depends(get_db)], user_id: int):
    task = db.scalars(select(Task).where(Task.user_id == user_id))
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='There is no user found'
        )
    else:
        return task

@router.post('/create')
async def create_task(db: Annotated[Session, Depends(get_db)], create_task: CreateTask, user_id: int):
    user_query = db.execute(select(User).where(User.id == user_id))
    user = user_query.scalars().first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User was not found")

    db.execute(insert(Task).values(
        title=create_task.title,
        content=create_task.content,
        priority=create_task.priority,
        user_id=user_id,
        slug=slugify(create_task.title)))
    db.commit()
    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}

@router.put('/update')
async def update_task(db: Annotated[Session, Depends(get_db)], update_task: UpdateTask, user_id: int):
    user = db.scalars(select(Task).where(Task.user_id == user_id))
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='There is no user found'
        )

    db.execute(update(Task).where(Task.id == user_id).values(
        title=update_task.title,
        content=update_task.content,
        priority=update_task.priority))
    db.commit()
    return {'status_code': status.HTTP_200_OK, 'transaction': 'User update is successful!'}

@router.delete('/delete')
async def delete_task(db: Annotated[Session, Depends(get_db)], user_id: int):
    user = db.scalars(select(Task).where(Task.user_id == user_id))
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='There is no user found'
        )

    try:
        db.execute(delete(Task).where(Task.id == user_id))
        db.commit()
        return {'status_code': status.HTTP_200_OK, 'transaction': 'User delete is successful!'}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred."
        )
