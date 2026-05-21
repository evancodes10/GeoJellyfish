from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from backend.routers import hab

app = FastAPI(title="GeoJellyfish API")

app.include_router(hab.router)

@app.get("/health")

def health_check():
    return {"status": "ok", "message": "GeoJellyfish API is running"}