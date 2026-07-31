from fastapi import FastAPI

from src.routes import router

app = FastAPI(
    title="Smart Expense Tracker API",
    version="1.0.0",
)

app.include_router(router)


@app.get("/")
def root():
    return {
        "message": "Smart Expense Tracker API"
    }