# app/api/v1/students.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db import models
from app.core.deps import get_current_user


router = APIRouter()

@router.get("/")
async def get_students():
    return {"message": "Students API is working!"}


@router.get("/me")
def get_my_profile(current_user: str = Depends(get_current_user), db: Session = Depends(get_db)):
    """Return details of the currently logged-in student"""
    user = db.query(models.Student).filter(models.Student.email == current_user).first()
    if not user:
        return {"error": "User not found"}
    
    return {
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "gender": str(user.gender.value) if user.gender else None,
        "status": str(user.status.value),
        "semester": user.semester,
        "degree_program": user.degree_program,
        "degree_name": user.degree_name,
        "department": user.department,
    }
