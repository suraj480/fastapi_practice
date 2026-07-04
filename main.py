from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def Home():
    return {"message": "Welcome to the FastAPI application!"}

@app.get("/about")
def About():
    return {"message": "This is a About page"}

@app.get("/users/{/user_id}")
def get_users(user_id):
    return {    "user_id": user_id, "message": f"User ID is {user_id}" }