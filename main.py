from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    price: float

items={
    "name":"chair",
    "price":350
}

@app.get("/items/{item_id}")
def get_item_by_id(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    return {"message": "Item not found"}

@app.get("/items/name/{name}")
def get_item_by_name(name: str):
    for item in items:
        if item.name == name:
            return item
    return {"message": "Item not found"}

@app.post("/items")
def create_item(item: Item):
    for existing_item in items:
        if existing_item.id == item.id:
            return {"message": "Item with this ID already exists"}
    items.append(item)
    return items

@app.put("/items/{item_id}")
def update_item(item_id: int, updated_item: Item):
    for item in items:
        if item.id == item_id:
            if updated_item.name is not None:
                item.name = updated_item.name
            if updated_item.price is not None:
                item.price = updated_item.price
            return item
    return {"message": "Item not found"}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for item in items:
        if item.id == item_id:
            items.remove(item)
            return item
    return {"message": "Item not found"}
