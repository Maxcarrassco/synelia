from sqlalchemy import String
from models import base_model
from sqlalchemy.orm import Mapped, mapped_column

class Class(base_model.BaseModel):
    __tablename__ = "class"
    label: Mapped[str] = mapped_column(String(250))

