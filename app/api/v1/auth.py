from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.db import models
from app.db.session import get_db
from app.core.security import hash_password, verify_password, create_access_token
from pydantic import BaseModel

router = APIRouter()


# Schema for signup
class UserCreate(BaseModel):
    username: str
    email: str
    password: str


@router.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(models.Student).filter(models.Student.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = models.Student(
        username=user.username,
        email=user.email,
        hashed_password=hash_password(user.password),
        status="active",
        semester=1,
        degree_program="BS",
        degree_name="Software Engineering",
        department="CS"
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "Signup successful", "user_id": new_user.id}


# ✅ Updated login route — works with Swagger “Authorize”
@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    db_user = db.query(models.Student).filter(models.Student.email == form_data.username).first()
    if not db_user or not verify_password(form_data.password, db_user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    token = create_access_token({"sub": db_user.email})
    return {"access_token": token, "token_type": "bearer"}
