from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import Annotated
from sqlalchemy import insert, select, update, delete
from slugify import slugify

from app.bakend.db_depends import get_db
from app.models import *
from app.schemas import CreateTask, UpdateTask

router = APIRouter(prefix='/task', tags=['task'])