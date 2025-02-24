from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List


app = FastAPI()

# define a item
class Item(BaseModel):
  id: int
  name: str
  description: str = None
  price: float
  status: bool
  
# create a fake database
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
  return {"Message": "Item added successfully", "item": item}

# read all the items
@app.get("/items/", response_model=List[Item])
def get_items():
  return list(database.values)

# read a single item
@app.get("/items/{item_id}")
def get_item(item_id: int):
  if item_id not in database:
    raise HTTPException(status=404, detail="Item not found")
  return database[item_id]

# update an item
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
  if item_id not in database:
    raise HTTPException(status=404, detail="Item {item} is not in databse")
  database[item_id] = item
  return {"Message": "Item updated successfully", "item": item}

# delete an item
app.delete("/items/{item_id}")
def delete_item(item_id: int):
  if item_id not in database:
    raise HTTPException(status_code=404, detail="Item {item} is not in database")
  del database[item_id]
  return {"Message: item deleted succesfully"}