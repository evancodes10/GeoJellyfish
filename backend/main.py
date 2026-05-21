from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="GeoJellyfish API")

@app.get("/health")

def health_check():
    return {"status": "ok", "message": "GeoJellyfish API is running"}