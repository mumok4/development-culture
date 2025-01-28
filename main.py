from fastapi import FastAPI

app=FastAPI()


@app.get("/")
def read_root():
    return {"message":"hello world"}

@app.get("/items")
def get_items():
    return {"items": ["item1", "item2", "item3"]}

@app.get("/items/{item_id}")
def get_item_by_id(item_id: int):
    return {"item": f"item{item_id}"}
