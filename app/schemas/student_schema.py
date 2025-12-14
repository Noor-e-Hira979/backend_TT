from pydantic import BaseModel, EmailStr
from typing import Optional
from enum import Enum

class Gender(str, Enum):
    male = "Male"
    female = "Female"
    other = "Other"

class Status(str, Enum):
    active = "Active"
    inactive = "Inactive"

class StudentCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    first_name: str
    last_name: str
    gender: Gender
    status: Status = Status.active
    semester: int
    degree_program: str
    degree_name: str
    department: str

class StudentLogin(BaseModel):
    email: EmailStr
    password: str

class StudentResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    first_name: str
    last_name: str
    gender: Gender
    status: Status
    semester: int
    degree_program: str
    degree_name: str
    department: str

    class Config:
        orm_mode = True
