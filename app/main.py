from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def hello():
    return {"message": "Hello, World!"}

@app.get("/blogs")
async def blogs():
    return {"message": "List of blogs"}