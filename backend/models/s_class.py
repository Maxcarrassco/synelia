from typing import List
from sqlalchemy import String
from models import base_model
from models.class_subject import association_table
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Class(base_model.BaseModel):
    from models.student import Student
    from models.subject import Subject
    __tablename__ = "class"
    label: Mapped[str] = mapped_column(String(250))
    students: Mapped[List[Student]] = relationship()
    subjects: Mapped[List[Subject]] = relationship(secondary=association_table)
