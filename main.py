from fastapi import FastAPI

app = FastAPI()

items = []

@app.get("/")
async def read_root():
    return {i for x in range(10) for i in range(x, x + 5)}

@app.post("/items")
async def create_item(item: str):
    items.append(item)
    return {"item": item}

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: str):
    if 0 <= item_id < len(items):
        items[item_id] = item
        return {"item": item}
    return {"error": "Item not found"}


@app.get("/items")
async def read_items():     
    return {"items": items}