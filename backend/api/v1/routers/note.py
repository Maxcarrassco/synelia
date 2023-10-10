#!/usr/bin/python3

from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from models import storage
from models.note import Note
from models.student import Student
from schemas.schemas import NoteSchema
from schemas.schemas import NoteStudId

note_router = APIRouter(prefix="/api/v1/notes", tags=["Notes"])

@note_router.get("/")
def get_notes():
    try:
        notes = [ v.to_dict() for _, v in storage.all(Note).items()]
    except Exception:
        raise HTTPException(500, detail="Oops! Something went wrong! We are working on it!")
    return notes


@note_router.post("/", status_code=201)
def create_note(note: NoteSchema):
    student = storage.get_obj_by_id(Student, note.student_id)
    if not student:
        return JSONResponse({ "msg": "User not Found" }, 404)
    try:
        Note(**(note.__dict__))
        storage.save()
    except Exception as err:
        print(err)
        raise HTTPException(500, detail="Oops! Something went wrong! We are working on it!")
    return { "msg": "Note Successfully created!"}



@note_router.get("/{id}")
def get_note(id: int):
    try:
        note = storage.get_obj_by_id(Note, id)
    except Exception:
        raise HTTPException(500, detail="Oops! Something went wrong! We are working on it!")
    if not note:
        return JSONResponse({ "msg": "Note not Found" }, 404)
    return note.to_dict()



@note_router.put("/{id}", status_code=204)
def update_note(id: int, note: NoteSchema):
    student = storage.get_obj_by_id(Student, note.student_id)
    if not student:
        return JSONResponse({ "msg": "User not Found" }, 404)
    note_db = storage.get_obj_by_id(Note, id)
    if not note_db:
        return JSONResponse({ "msg": "Note not Found" }, 404)
    note_db.student_id = note.student_id
    note_db.note = note.note
    try:
        storage.update(note_db, id)
        storage.save()
    except Exception:
        raise HTTPException(500, detail="Oops! Something went wrong! We are working on it!")
    return b""


@note_router.delete("/{id}")
def delete_note(student: NoteStudId, id: int):
    student = storage.get_obj_by_id(Student, student.student_id)
    if not student:
        return JSONResponse({ "msg": "User not Found" }, 404)
    note = storage.get_obj_by_id(Note, id)
    if not note:
        return JSONResponse({ "msg": "Note not Found" }, 404)
    try:
        storage.delete(note)
        storage.save()
    except Exception:
        raise HTTPException(500, detail="Oops! Something went wrong! We are working on it!")
    return note.to_dict()
