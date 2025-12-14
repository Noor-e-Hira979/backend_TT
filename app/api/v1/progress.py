from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db import models
from app.schemas.progress_schema import ProgressCreate, ProgressResponse

router = APIRouter()

@router.post("/submit", response_model=ProgressResponse)
def create_progress(data: ProgressCreate, db: Session = Depends(get_db)):
    student_id = 1  # temporary

    progress = models.Progress(
        student_id=student_id,
        labs_completed=data.labs_completed,
        assignments_completed=data.assignments_completed,
        quizzes_completed=data.quizzes_completed,
        skills=data.skills,
        interests=data.interests,
        preferred_domain=data.preferred_domain,
    )

    db.add(progress)
    db.commit()
    db.refresh(progress)

    return progress


# ---------------- NEW ROUTE -------------------------
@router.get("/latest/{student_id}", response_model=ProgressResponse)
def get_latest_progress(student_id: int, db: Session = Depends(get_db)):

    progress = (
        db.query(models.Progress)
        .filter(models.Progress.student_id == student_id)
        .order_by(models.Progress.id.desc())
        .first()
    )

    if not progress:
        raise HTTPException(status_code=404, detail="No progress found")

    return progress
