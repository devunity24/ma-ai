from fastapi import FastAPI
from app.routes import doubts

app = FastAPI()

app.include_router(doubts.router, tags=["Doubt"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI app!"}
