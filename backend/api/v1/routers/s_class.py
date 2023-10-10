#!/usr/bin/python3

from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from models import storage
from models.s_class import Class
from schemas.schemas import ClassSchema

class_router = APIRouter(prefix="/api/v1/classes", tags=["Class"])

@class_router.get("/")
def get_classes():
    try:
        classes = [ v.to_dict() for _, v in storage.all(Class).items()]
    except Exception:
        raise HTTPException(500, detail="Oops! Something went wrong! We are working on it!")
    return classes


@class_router.post("/", status_code=201)
def create_classe(classe: ClassSchema):
    try:
        Class(**(classe.__dict__))
        storage.save()
    except Exception:
        raise HTTPException(500, detail="Oops! Something went wrong! We are working on it!")
    return { "msg": "Class Successfully created!"}



@class_router.get("/{id}")
def get_classe(id: int):
    try:
        classe = storage.get_obj_by_id(Class, id)
    except Exception:
        raise HTTPException(500, detail="Oops! Something went wrong! We are working on it!")
    if not classe:
        return JSONResponse({ "msg": "Class not Found" }, 404)
    return classe.to_dict()



@class_router.put("/{id}", status_code=204)
def update_classe(id: int, classes: ClassSchema):
    classe = storage.get_obj_by_id(Class, id)
    if not classe:
        return JSONResponse({ "msg": "Class not Found" }, 404)
    classe.label = classes.label
    try:
        storage.update(classe, id)
        storage.save()
    except Exception:
        raise HTTPException(500, detail="Oops! Something went wrong! We are working on it!")
    return b""


@class_router.delete("/{id}")
def delete_classe(id: int):
    classe = storage.get_obj_by_id(Class, id)
    if not classe:
        return JSONResponse({ "msg": "Class not Found" }, 404)
    try:
        storage.delete(classe)
        storage.save()
    except Exception:
        raise HTTPException(500, detail="Oops! Something went wrong! We are working on it!")
    return classe.to_dict()
