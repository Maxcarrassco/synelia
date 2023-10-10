from typing import Any
from sqlalchemy import BigInteger, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import datetime
from random import randint


class BaseModel(DeclarativeBase):
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
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
        from models import storage
        storage.new(self)

    def __str__(self) -> str:
        return f"({self.__class__.__name__}) {self.to_dict()}"
    
    def __repr__(self) -> str:
        return f"({self.__class__.__name__}) {self.to_dict()}"


    def to_dict(self):
        data = self.__dict__.copy()
        del data["_sa_instance_state"]
        data["created_at"] = data["created_at"].isoformat()
        if data["updated_at"]:
            data["updated_at"] = data["updated_at"].isoformat()
        return data
