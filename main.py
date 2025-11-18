from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# 1. Define the Shape of the Data (The "Schema")
# This tells Python: "Expect a JSON with a username and password"
class LoginRequest(BaseModel):
    username: str
    password: str

@app.get("/")
def read_root():
    return {"status": "Online"}

# 2. The Login Logic
@app.post("/login")
def login(data: LoginRequest):
    # Print what we received (so you can see it in the PyCharm terminal)
    print(f"Received login attempt: {data.username}")

    # SIMPLE LOGIC (We will connect a real database later)
    if data.username == "admin" and data.password == "123456":
        return {"status": "success", "message": "Welcome back, Admin!"}
    else:
        # If wrong, send a 401 Error
        raise HTTPException(status_code=401, detail="Wrong username or password")