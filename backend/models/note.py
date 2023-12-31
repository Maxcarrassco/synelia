from sqlalchemy import ForeignKey, String, TEXT
from models import base_model
from sqlalchemy.orm import Mapped, mapped_column

class Note(base_model.BaseModel):
    __tablename__ = "notes"
    note: Mapped[str] = mapped_column(TEXT)
    student_id: Mapped[int] = mapped_column(ForeignKey("students.id"))
