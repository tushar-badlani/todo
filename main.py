from fastapi import FastAPI

app = FastAPI()

todos = []

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/todos")
async def get_todos():
    return todos

@app.post("/todos")
async def create_todo(todo: str):
    todos.append(todo)
    return todos

@app.delete("/todos")
async def delete_todo(todo: str):
    todos.remove(todo)
    return todos

@app.put("/todos")
async def update_todos(todo: str, new_todo: str):
    todos.remove(todo)
    todos.append(new_todo)
    return todos

