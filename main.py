from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def Home():
    return {"message": "Welcome to the FastAPI application!"}

@app.get("/about")
def About():
    return {"message": "This is a About page"}

# Dynamic route with path parameter

# @app.get("/users/{/user_id}")
# def get_users(user_id):
#     return {    "user_id": user_id, "message": f"User ID is {user_id}" }

# Query parameter example
@app.get("/search") 
def search(query: str):
    return {"query": query, "message": f"Search results for '{query}'"}

@app.get("/items")
def get_items(price: int, name: str = None):
    if name:
        return {"price": price, "name": name, "message": f"Item '{name}' with price {price}"}
    else:
        return {"price": price, "message": f"Item with price {price}"}