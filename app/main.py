from fastapi import FastAPI

from app.core.config import settings

app = FastAPI(
    title=settings.project_name,
    description="Backend API for vehicle maintenance tracking",
    version=settings.version,
    debug=settings.debug,
)


@app.get("/")
def read_root():
    return {"message": f"Welcome to {settings.project_name}"}


@app.get("/health")
def health_check():
    return {"status": "ok"}