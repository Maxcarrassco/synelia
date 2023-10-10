from pydantic import BaseModel
from enum import Enum


class Gender(Enum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"


class StudentSchema(BaseModel):
    name: str
    gender: Gender

class NoteSchema(BaseModel):
    note: str
    student_id: int

class ClassSchema(BaseModel):
    label: str

class SubjectSchema(BaseModel):
    label: str

class NoteStudId(BaseModel):
    student_id: int
