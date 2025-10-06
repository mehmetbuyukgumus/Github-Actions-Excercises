from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def hello():
    return {"message": "Hello, World!"}

@app.get("/blogs")
async def blogs():
    return {"message": "List of blogs"}

@app.get("about")
async def about():
    return {"message": "About page"}