"""
=========================================================
            FASTAPI COMPLETE LEARNING FILE
=========================================================

Topics Covered

1. Basic GET API
2. Path Parameters
3. Query Parameters
4. POST API
5. Pydantic Models
6. Nested Pydantic Models

Run

uvicorn app:app --reload

Swagger

http://127.0.0.1:8000/docs
=========================================================
"""

from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

# -------------------------------------------------------
# Creating FastAPI Application
# -------------------------------------------------------

app = FastAPI(
    title="FastAPI Learning",
    description="Learning FastAPI Step by Step",
    version="1.0"
)

# =======================================================
# 1. BASIC GET APIs
# =======================================================

@app.get("/")
def home():
    """
    Home Endpoint

    URL:
    /

    Method:
    GET
    """

    return {
        "message": "Welcome to FastAPI"
    }


@app.get("/about")
def about():
    """
    About Endpoint
    """

    return {
        "message": "This is About Page"
    }


# =======================================================
# 2. PATH PARAMETERS
# =======================================================

@app.get("/users/{user_id}")
def get_user(user_id: int):
    """
    Path Parameter

    URL

    /users/10

    Output

    {
        "user_id":10
    }
    """

    return {
        "user_id": user_id,
        "message": f"User ID is {user_id}"
    }


# =======================================================
# 3. QUERY PARAMETERS
# =======================================================

@app.get("/search")
def search(query: str):
    """
    Required Query Parameter

    URL

    /search?query=python
    """

    return {
        "query": query,
        "message": f"Searching for {query}"
    }


@app.get("/items")
def get_items(price: int, name: Optional[str] = None):
    """
    Optional Query Parameter

    Examples

    /items?price=100

    /items?price=100&name=Laptop
    """

    if name:

        return {
            "price": price,
            "name": name
        }

    return {
        "price": price
    }


# =======================================================
# 4. PYDANTIC MODEL
# =======================================================

class User(BaseModel):
    """
    Simple Request Body
    """

    name: str
    age: int


@app.post("/create-user")
def create_user(user: User):
    """
    POST API Example

    Body

    {
        "name":"Suraj",
        "age":25
    }
    """

    return {
        "message": "User Created Successfully",
        "data": user
    }


# =======================================================
# 5. NESTED PYDANTIC MODEL
# =======================================================

class Address(BaseModel):
    city: str
    state: str
    pincode: str


class UserWithAddress(BaseModel):
    name: str
    age: int
    address: Address


@app.post("/create-user-with-address")
def create_user_with_address(user: UserWithAddress):
    """
    Nested Request Body

    {
        "name":"Suraj",
        "age":25,
        "address":{
            "city":"Mumbai",
            "state":"Maharashtra",
            "pincode":"400001"
        }
    }
    """

    return {
        "message": "User Created Successfully",
        "user": user
    }


# =======================================================
# END OF FILE
# =======================================================