from sqlalchemy import String
from models import base_model
from sqlalchemy.orm import Mapped, mapped_column

class Student(base_model.BaseModel):
    __tablename__ = "students"
    name: Mapped[str] = mapped_column(String(250))
    gender: Mapped[str] = mapped_column(String(250))

