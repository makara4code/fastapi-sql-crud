from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"message": "Hello"}


@app.post("/todos")
def get_todo():
    return {"message": "TOdo"}
