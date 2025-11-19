from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class LoginRequest(BaseModel):
    username: str
    password: str

@app.get("/")
def read_root():
    return {"status": "Online"}

@app.post("/login")
def login(data: LoginRequest):
    print(f"Received login attempt: {data.username}")

    if data.username == "admin" and data.password == "123456":
        return {"status": "success", "message": "Welcome back, Admin!"}
    else:
        raise HTTPException(status_code=401, detail="Wrong username or password")