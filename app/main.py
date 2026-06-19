from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.router import main_router
from app.utils.exceptions import AppException, app_exception_handler
from app.middleware.pagination import PaginationMiddleware

app = FastAPI(title="Inventory & Order Management API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_exception_handler(AppException, app_exception_handler)
app.add_middleware(PaginationMiddleware)

app.include_router(main_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Inventory & Order Management API"}

