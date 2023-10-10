from typing import Any
from sqlalchemy import func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import datetime
from random import randint


class BaseModel(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime | None] = mapped_column(onupdate=func.now())

    
    def __init__(self, **kwargs: Any):
        if kwargs:
            for key, val in kwargs.items():
                setattr(self, key, val)
            if "created_at" not in kwargs:
                self.created_at = datetime.utcnow()
            if "updated_at" not in kwargs:
                self.updated_at = None
            if "id" not in kwargs:
                # Note uniqueness is not guarantee here but this match the constraint for the IDs to be 11 in length.
                # I could use uuid version 4 for uniqueness but it could satify the length constraint
                START = 11111111111 # the least possible id
                END = 99999999999 # the highest possible id
                self.id = randint(START, END)
        else:
            self.created_at = datetime.utcnow()
            self.updated_at = None
            # Note uniqueness is not guarantee here but this match the constraint for the IDs to be 11 in length.
            # I could use uuid version 4 for uniqueness but it could satify the length constraint
            START = 11111111111 # the least possible id
            END = 99999999999 # the highest possible id
            self.id = randint(START, END)


    def to_dict(self):
        data = self.__dict__.copy()
        del data["_sa_instance_state"]
        return data

