from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import Annotated
from sqlalchemy import insert, select, update, delete
from slugify import slugify

from app.bakend.db_depends import get_db
from app.models import *
from app.schemas import CreateUser, UpdateUser

router = APIRouter(prefix="/user", tags=["user"])

@router.get('/')
async def all_users(db: Annotated[Session, Depends(get_db)]):
    users = db.scalars(select(User)).all()
    return users

@router.get('/user_id')
async def user_by_id(db: Annotated[Session, Depends(get_db)], user_id: int):
    user = db.scalars(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='There is no user found'
        )
    else:
        return user

@router.post('/create')
async def create_user(db: Annotated[Session, Depends(get_db)], create_user: CreateUser):
    user_query = db.execute(select(User).where(User.username == create_user.username))
    user = user_query.scalars().first()
    if user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User with this username already exists.")

    slug = create_user.username

    db.execute(insert(User).values(
        username=create_user.username,
        firstname=create_user.firstname,
        lastname=create_user.lastname,
        age=create_user.age,
        slug=slug))

    db.commit()
    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}

@router.put('/update')
async def update_user(db: Annotated[Session, Depends(get_db)], update_user: UpdateUser, user_id: int):
    user = db.scalars(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='There is no user found'
        )

    db.execute(update(User).where(User.id == user_id).values(
        firstname=update_user.firstname,
        lastname=update_user.lastname,
        age=update_user.age))
    db.commit()
    return {'status_code': status.HTTP_200_OK, 'transaction': 'User update is successful!'}

@router.delete('/delete')
async def delete_user(db: Annotated[Session, Depends(get_db)], user_id: int):
    user = db.scalars(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='There is no user found'
        )

    try:
        db.execute(delete(Task).where(Task.user_id == user_id))
        db.execute(delete(User).where(User.id == user_id))
        db.commit()
        return {'status_code': status.HTTP_200_OK, 'transaction': 'User delete is successful!'}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred."
        )
