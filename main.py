from pydoc import describe
from typing import Union
from unittest import result
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name:str
    description: Union[str, None] = None
    price = float
    tax: Union[float, None] = None

app = FastAPI()

@app.put("/items/{item_id}")
async def create_item(item_id: int, item:Item, q: Union[str, None] = None):
    result = {"item_id": item_id, **item_dict()}
    if q:
        result.update({"q":q})
    return result