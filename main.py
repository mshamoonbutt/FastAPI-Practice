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