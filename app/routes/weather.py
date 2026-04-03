from fastapi import APIRouter, HTTPException
from app.services.weather_service import fetch_weather

router = APIRouter()

@router.get("/weather")
def get_weather(city: str):
    from fastapi import APIRouter, HTTPException
from app.services.weather_service import fetch_weather

router = APIRouter()

@router.get("/weather")
def get_weather(city: str):

    # ✅ Validación primero
    if not city:
        raise HTTPException(status_code=400, detail="City is required")

    try:
        return fetch_weather(city)

    except HTTPException as e:
        # ya viene bien formateado
        raise e

    except Exception:
        # error inesperado (backend)
        raise HTTPException(status_code=500, detail="Internal server error")