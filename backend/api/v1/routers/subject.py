#!/usr/bin/python3

from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from models import storage
from models.subject import Subject
from schemas.schemas import SubjectSchema

subject_router = APIRouter(prefix="/api/v1/sujects", tags=["Subjects"])

@subject_router.get("/")
def get_sujects():
    try:
        sujects = [ v.to_dict() for _, v in storage.all(Subject).items()]
    except Exception:
        raise HTTPException(500, detail="Oops! Something went wrong! We are working on it!")
    return sujects


@subject_router.post("/", status_code=201)
def create_subject(subject: SubjectSchema):
    try:
        Subject(**(subject.__dict__))
        storage.save()
    except Exception:
        raise HTTPException(500, detail="Oops! Something went wrong! We are working on it!")
    return { "msg": "Subject Successfully created!"}



@subject_router.get("/{id}")
def get_subject(id: int):
    try:
        subject = storage.get_obj_by_id(Subject, id)
    except Exception:
        raise HTTPException(500, detail="Oops! Something went wrong! We are working on it!")
    if not subject:
        return JSONResponse({ "msg": "Subject not Found" }, 404)
    return subject.to_dict()



@subject_router.put("/{id}", status_code=204)
def update_subject(id: int, subject: SubjectSchema):
    subject_db = storage.get_obj_by_id(Subject, id)
    if not subject_db:
        return JSONResponse({ "msg": "Subject not Found" }, 404)
    subject_db.label = subject.label
    try:
        storage.update(subject_db, id)
        storage.save()
    except Exception:
        raise HTTPException(500, detail="Oops! Something went wrong! We are working on it!")
    return b""


@subject_router.delete("/{id}")
def delete_subject(id: int):
    subject = storage.get_obj_by_id(Subject, id)
    if not subject:
        return JSONResponse({ "msg": "Subject not Found" }, 404)
    try:
        storage.delete(subject)
        storage.save()
    except Exception:
        raise HTTPException(500, detail="Oops! Something went wrong! We are working on it!")
    return subject.to_dict()
