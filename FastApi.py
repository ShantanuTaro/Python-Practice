from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def show_user():
    return "printed!"

@app.get("/user")
def get_user():
    return "User is 234"