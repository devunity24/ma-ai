from fastapi import FastAPI
from app.routes import doubts

app = FastAPI()

# Include routers
#app.include_router(users.router, prefix="/users", tags=["Users"])
#app.include_router(items.router, prefix="/items", tags=["Items"])

app.include_router(doubts.router, tags=["Doubt"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI app!"}
