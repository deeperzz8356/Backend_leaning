from typing import Optional

from fastapi import FastAPI

from pydantic import BaseModel

app=FastAPI()

@app.get("/")
def read_root():
    return {"Message":"Hello Deep"}

@app.get("/greet")
def greet():
    return {"Message":"Welcome to FastAPI"}

@app.get("/greet/{name}")
def greet_name(name:str, age: Optional[int]= None):
    return {"Message":f"Good morning {name} and You are {age} years old."}

class student(BaseModel):
    name:str
    age:int
    grade:str

@app.post("/student")
def create_student(student:student):
    return {
        "name": student.name,
        "age": student.age,
        "grade": student.grade
        }