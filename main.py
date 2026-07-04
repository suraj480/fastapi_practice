from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class User(BaseModel):
    username: str
    email: str
    age: int   

# @app.post("/create_user")    
# def create_user(user: User):
#     return {"message": f"User {user.username} created successfully!"}

class Address(BaseModel):
    city: str
    state: str
    pincode: str

class UserWithAddress(BaseModel):
    name:str
    age: int
    address: Address

@app.post("/create-user")    
def create_user(user: UserWithAddress):
    return {"message": f"User {user.name} created successfully!"}  