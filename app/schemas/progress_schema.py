from pydantic import BaseModel

class ProgressCreate(BaseModel):
    labs_completed: int
    assignments_completed: int
    quizzes_completed: int
    skills: str | None = None
    interests: str | None = None
    preferred_domain: str | None = None


class ProgressResponse(BaseModel):
    id: int
    student_id: int
    labs_completed: int
    assignments_completed: int
    quizzes_completed: int
    skills: str | None = None
    interests: str | None = None
    preferred_domain: str | None = None

    class Config:
        from_attributes = True   # NEW name in Pydantic v2
