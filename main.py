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


# Create an item
app.post("/items/")
def create_item(item: Item):
  if item.id in database:
    raise HTTPException(status=400, detail="Item already exists")
  database[item.id] = item
  return {"Message"}