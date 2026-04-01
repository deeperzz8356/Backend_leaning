from fastapi import FastAPI

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