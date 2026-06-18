from fastapi import FastAPI
from app.routers.router import main_router
from app.utils.exceptions import AppException, app_exception_handler

app = FastAPI(title="Inventory & Order Management API")

app.add_exception_handler(AppException, app_exception_handler)

app.include_router(main_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Inventory & Order Management API"}

