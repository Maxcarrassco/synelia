from typing import List
from sqlalchemy import ForeignKey, String
from models import base_model
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Student(base_model.BaseModel):
    from models.note import Note
    __tablename__ = "students"
    name: Mapped[str] = mapped_column(String(250))
    gender: Mapped[str] = mapped_column(String(250))
    class_id: Mapped[int] = mapped_column(ForeignKey("class.id"))
    notes: Mapped[List[Note]] = relationship()
