from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List


app = FastAPI()

# define a fake item

class Item(BaseModel):
  id: int
  name: str
  description: str = None
  price: float
  status: bool
  
# craete a fake database

database = {}

@app.get("/")
def home():
  return {"This is my first fast api site..."}


# Create