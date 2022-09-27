from ctypes import resize
from email.policy import default
from pydoc import describe
from typing import List, Union
from unittest import result
from fastapi import FastAPI, Query
from pydantic import BaseModel

class Item(BaseModel):
    name:str
    description: Union[str, None] = None
    price = float
    tax: Union[float, None] = None

app = FastAPI()

# @app.put("/items/")
# async def create_item(item:Item):
#     item_dict = item.dict()
#     if item.tax:
#         price_with_tax = item.price + item.tax
#         item_dict.update({"price_with_tax":price_with_tax})
#     return item_dict

# @app.put("/items/{item_id}")
# async def create_item(item_id:int, item:Item, q: Union[str, None] = None):
#     result = {"item_id":item_id, **item.dict()}
#     if q:
#         result.update({"q":q})
#     return result

# @app.get("/items/")
# async def read_items(q:Union[str, None] = None):
#     results = {"items": [{"item_id":"Foo"}, {"item_id":"Bar"}]}
#     if q:
#         results.update({"q":q})
#     return results

# @app.get("/items/")
# async def read_items(q: Union[str, None] = Query(default=None, max_length=50)):
#     results = {"items":[{"item_id":"Foo"}, {"item_id":"Bar"}]}
#     if q:
#         results.update({"q":q})
#     return results

# @app.get("/items/")
# async def read_items(q: Union[List[str], None] = Query(default= ["foo", "bar"])):
#     query_items = {"q":q}
#     return query_items

# @app.get("/items/")
# async def read_items(q:list = Query(default=[])):
#     query_items = {"q":q}
#     return query_items

# @app.get("/items/")
# async def read_items(
#     q:Union[str, None] = Query(
#         default=None,
#         title="Query string",
#         description="Query string for the items to search in the database that have a good match",
#         min_length=3,
#     )
# ):
#     results = {"items": [{"item_id":"Foo"}, {"item_id":"Bar"}]}
#     if q:
#         results.update({"q":q})
#     return results

@app.get("/items/")
async def read_items(
    q: Union[str, None] = Query(
        default=None,
        alias="item-query",
        title="Query string",
        description="Query string for the item to search in the database that have a good match",
        min_length=3,
        max_length=50,
        regex="^fixedquery$",
        deprecated=True,
    )
):
    results = {"items":[{"item_id":"Foo"}, {"item_id":"Bar"}]}
    if q:
        results.update({"q":q})
    return results