#!/usr/bin/python3

from typing import List, Optional
from sqlalchemy import ForeignKey, String
from models import base_model
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Student(base_model.BaseModel):
    from models.note import Note
    __tablename__ = "students"
    name: Mapped[str] = mapped_column(String(250))
    gender: Mapped[str] = mapped_column(String(250))
    class_id: Mapped[Optional[int]] = mapped_column(ForeignKey("class.id"))
    classes: Mapped[Optional["Class"]] = relationship(back_populates="students")
    notes: Mapped[List[Note]] = relationship()
