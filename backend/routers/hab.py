from fastapi import APIRouter

router = APIRouter(prefix="/hab", tags=["HAB Alerts"])

@router.get("/")

def get_hab_alerts(lat: float, lon: float):
    return {
        "lat": lat,
        "lon": lon,
        "alert_level": 2,
        "label": "Moderate Bloom",
        "color": "orange",
        "description": "Jellyfish and HAB activity detected in this area."
    }