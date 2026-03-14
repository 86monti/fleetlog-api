from fastapi import Depends, FastAPI
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.database import get_db

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


@app.get("/db-check")
def db_check(db: Session = Depends(get_db)):
    db.execute(text("SELECT 1"))
    return {"message": "database connection successful"}