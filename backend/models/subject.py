#!/usr/bin/python3

from sqlalchemy import String
from models import base_model
from sqlalchemy.orm import Mapped, mapped_column

class Subject(base_model.BaseModel):
    __tablename__ = "subjects"
    label: Mapped[str] = mapped_column(String(250))

