from fastapi import FastAPI
from app.routes import users, items

app = FastAPI()

# Include routers
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(items.router, prefix="/items", tags=["Items"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI app!"}
