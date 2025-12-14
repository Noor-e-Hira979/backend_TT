from sqlalchemy import Column, Integer, String, Boolean, Enum
from app.db.session import Base
from enum import Enum as PyEnum
from sqlalchemy import ForeignKey

class Gender(PyEnum):
    male = "Male"
    female = "Female"
    other = "Other"

class Status(PyEnum):
    active = "Active"
    inactive = "Inactive"

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(Enum(Gender))
    status = Column(Enum(Status), default=Status.active)
    semester = Column(Integer)
    degree_program = Column(String)
    degree_name = Column(String)
    department = Column(String)

# ----------------- Progress Model -----------------
class Progress(Base):
    __tablename__ = "progress"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)

    labs_completed = Column(Integer, default=0)
    assignments_completed = Column(Integer, default=0)
    quizzes_completed = Column(Integer, default=0)

    skills = Column(String, nullable=True)     # store CSV string like "React,Python"
    interests = Column(String, nullable=True)
    preferred_domain = Column(String, nullable=True)
