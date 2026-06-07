from fastapi import FastAPI,status
from fastapi.exceptions import HTTPException
from pydantic import BaseModel

books = [
{
"id" : 1,
"title": "The Alchemist",
"author": "Paulo Coelho",
"publish_date": "1988-01-01"},
{
"id": 2,
"title": "The God of Small Things", 
"author": "Arundhati Roy",
"publish_date": "1997-04-04"
},
{
"id": 3,
"title": "The White Tiger",
"author": "Aravind Adiga",
"publish_date": "2008-01-01"}
 ,{   
   "id": 4,
    "title": "The Palace of Illusions",
    "author": "Chitra Banerjee Divakaruni",
    "publish_date": "2008-02-12"}
]


app=FastAPI()

@app.get("/books")
def get_books():
    return books

@app.get("/books/{book_id}")
def get_book(book_id:int):
    for book in books:
        if book["id"]==book_id:
            return book
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

class book(BaseModel):
    id:int
    title:str
    author:str
    publish_date:str
    
    
    
@app.post("/add_book")
def add_books(book:book):
    books.append(book.model_dump())
    return "Books added successfully"

class update_book(BaseModel):
    title:str
    author:str
    publish_date:str
    

@app.put("/books/{books_id}")
def update_books(book_id:int, book_new:update_book):
    for book in books:
        if book["id"]==book_id:
            book["title"]=book_new.title
            book["author"]=book_new.author
            book["publish_date"]=book_new.publish_date
            return "Book updated successfully"
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
        
@app.delete("/books/{book_id}")
def delete_book(book_id:int):
    global books
    books = [book for book in books if book["id"] != book_id]
    return "Book deleted successfully"
