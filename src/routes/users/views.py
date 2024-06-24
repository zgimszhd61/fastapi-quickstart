# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from . import models, schemas
# from .database import get_db

# router = APIRouter()

# @router.post("/users/", response_model=schemas.User)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     db_user = models.User(username=user.username, email=user.email)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user

# @router.get("/users/{user_id}", response_model=schemas.User)
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = db.query(models.User).filter(models.User.id == user_id).first()
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user

from fastapi import APIRouter

router = APIRouter()

@router.get("/users")
def read_items():
    return {"users": ["item1", "item2"]}