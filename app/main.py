from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str

DB = {}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/items")
def create_item(item: Item):
    DB[item.id] = item.name
    return {"created": item}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    name = DB.get(item_id)
    if name is None:
        return {"error": "not found"}
    return {"id": item_id, "name": name}
