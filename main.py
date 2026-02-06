from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class student(BaseModel):
    name: str
    email: str
    age: int
    roll_number: int
    Department: str

class StudentResponse(BaseModel):
    name: str
    email: str
    age: int
    roll_number: int
    Department: str

@app.get("/")
def read_root():
    return {"Hello": "World"}
def create_student(student: student):
    return student


def read_student():
    return studentResponse(id=id, **student.dict())

def update_student():
    return studentResponse(id=id, **student.dict())

def delete_student():
    return studentResponse(id=id, **student.dict())


@app.post("/students")
def create_student(student:student):
    return create_student(student)

@app.get("/students/{id}")
def read_student(id:int):
    return read_student(id)

@app.put("/students/{id}")
def update_student(id:int,student:student):
    return update_student(id,student)

@app.delete("/students/{id}")
def delete_student(id:int):
    return delete_student(id)
