from fastapi import APIRouter, Depends
from dependencies import get_db

# NOTE : to add new router, add the file_name to app.py too.

admin_router = APIRouter(
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_db)],
    responses={404: {"description": "Not found"}},
)

user_router = APIRouter(
    prefix="/user",
    tags=["user"],
    dependencies=[Depends(get_db)],
    responses={404: {"description": "Not found"}},
)
auth_router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    dependencies=[Depends(get_db)],
    responses={404: {"description": "Not found"}},
)



