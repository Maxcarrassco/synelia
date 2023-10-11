#!/usr/bin/python3

from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from models import storage
from models.student import Student
from schemas.schemas import StudentSchema

student_router = APIRouter(prefix="/api/v1/students", tags=["Students"])

@student_router.get("/")
def get_students():
    try:
        students = [ v.to_dict() for _, v in storage.all(Student).items()]
    except Exception:
        raise HTTPException(500, detail="Oops! Something went wrong! We are working on it!")
    return students


@student_router.post("/", status_code=201)
def create_student(student: StudentSchema):
    try:
        stud = Student(**(student.__dict__))
        stud.gender = student.gender.value
        storage.save()
    except Exception:
        raise HTTPException(500, detail="Oops! Something went wrong! We are working on it!")
    return { "msg": "Student Successfully created!"}



@student_router.get("/{id}")
def get_student(id: int):
    try:
        student = storage.get_obj_by_id(Student, id)
    except Exception:
        raise HTTPException(500, detail="Oops! Something went wrong! We are working on it!")
    if not student:
        return JSONResponse({ "msg": "Student not Found" }, 404)
    return student.to_dict()



@student_router.put("/{id}", status_code=204)
def update_student(id: int, stud: StudentSchema):
    student = storage.get_obj_by_id(Student, id)
    if not student:
        return JSONResponse({ "msg": "Student not Found" }, 404)
    student.gender = stud.gender.value
    student.name = stud.name
    student.age = stud.age;
    try:
        storage.update(student, id)
        storage.save()
    except Exception:
        raise HTTPException(500, detail="Oops! Something went wrong! We are working on it!")
    return b""


@student_router.delete("/{id}")
def delete_student(id: int):
    student = storage.get_obj_by_id(Student, id)
    if not student:
        return JSONResponse({ "msg": "Student not Found" }, 404)
    try:
        storage.delete(student)
        storage.save()
    except Exception:
        raise HTTPException(500, detail="Oops! Something went wrong! We are working on it!")
    return student.to_dict()
