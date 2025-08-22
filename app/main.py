from fastapi import FastAPI
from app.routes.users import router as users_router
import logging
app = FastAPI(
    title="User Management API",
    description="A clean FastAPI application with repository pattern",
    version="1.0",
)
logger = logging.getLogger("uvicorn.error")
app.include_router(users_router)

@app.get("/")
def root():
    logger.info("Inside / endpoint")

    return {"message": app.title}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)