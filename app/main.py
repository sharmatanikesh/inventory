from fastapi import FastAPI

app = FastAPI(title="Inventory & Order Management API")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Inventory & Order Management API"}
