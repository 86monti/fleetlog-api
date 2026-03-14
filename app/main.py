from fastapi import FastAPI

app = FastAPI(
    title="FleetLog API",
    description="Backend API for vehicle maintenance tracking",
    version="0.1.0",
)


@app.get("/")
def read_root():
    return {"message": "Welcome to FleetLog API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}