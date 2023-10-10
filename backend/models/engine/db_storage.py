import os
from typing import Union
from dotenv import load_dotenv as _
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.student import Student
from models.note import Note
from models.subject import Subject
from models.s_class import Class
from models.base_model import BaseModel

DBURL = os.environ["DB_URL"]

class DBStorage:
    __session = None
    __engine = None

    def __init__(self) -> None:
        self.__engine = create_engine(DBURL, pool_pre_ping=True)

    def new(self, ob: Union[Class, Student, Note, Subject]):
        """Add new objects to the current db session"""
        if not self.__session:
            return
        self.__session.add(ob)

    def reload(self):
        """Init the db"""
        if not self.__engine:
            return
        BaseModel.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def save(self):
        """Commit the current session to db"""
        if not self.__session:
            return
        try:
            self.__session.commit()
        except Exception:
            self.__session.rollback()

    def all(self, ob: Union[Class, Student, Note, Subject], offset: int = 0, limit: int = 40):
        """Get the specific list of objects or all types of object from db"""
        objs={}
        if not self.__session:
            return objs
        if not ob:
            for model in [Class, Student, Note, Subject]:
                result = self.__session.query(model).offset(offset).limit(limit).all()
                for obj in result:
                    key = f"{type(model).__name__}.{obj.id}"
                    objs[key] = obj
            return objs
        result = self.__session.query(ob).offset(offset).limit(limit).all()
        for obj in result:
            key = f"{type(obj).__name__}.{obj.id}"
            objs[key] = obj
        return objs


    def close_session(self):
        """Close he current session"""
        if not self.__session:
            return
        self.__session.close()
