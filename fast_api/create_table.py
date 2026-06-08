# create_table.py
from database import engine, Base
from model import Book   # <-- this import is critical!

Base.metadata.create_all(bind=engine)
