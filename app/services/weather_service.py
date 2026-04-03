import requests
import os
import json
from fastapi import HTTPException

from app.config.redis import redis_client



API_KEY = os.getenv("WEATHER_API_KEY")
BASE_URL = os.getenv("WEATHER_API_URL")


def fetch_weather(city: str):
    cache_key = f"weather:{city.lower()}"

    # 1. Intentar obtener desde cache
    try:
        cached = redis_client.get(cache_key)
        if cached:
            return {
                "source": "cache",
                "data": json.loads(cached)
            }
    except:
        pass

    # 2. Llamar API externa
    url = f"{BASE_URL}/{city}?unitGroup=metric&key={API_KEY}&contentType=json"
    response = requests.get(url, timeout=5)

    if response.status_code != 200:
        print("STATUS:", response.status_code)
        print("RESPONSE:", response.text)
        print("API_KEY:", API_KEY)
        print("URL:", url)
        raise HTTPException(status_code=502, detail="Weather service unavailable")

    data = response.json()

    current_day = data.get("days", [{}])[0]

    description_map = {
        "Partially cloudy": "Parcialmente nublado",
        "Clear": "Despejado",
        "Rain": "Lluvia"
    }

    raw_description = current_day.get("conditions")

    description = description_map.get(
        raw_description,
        raw_description  # fallback si no existe traducción
    )

    clean_data = {
        "city": data.get("resolvedAddress"),
        "temperature": current_day.get("temp"),
        "description": description,
        "humidity": current_day.get("humidity"),
        "wind_speed": current_day.get("windspeed"),
        "rain_probability": current_day.get("precipprob"),
        "hourly": [
            {
                "time": h.get("datetime"),
                "temperature": h.get("temp"),
                "conditions": h.get("conditions")
            }
            for h in current_day.get("hours", [])[:24]
        ]
    }

    # 3. Guardar en cache (12 horas)
    try:
        redis_client.setex(
            cache_key,
            43200,
            json.dumps(clean_data)
        )
    except:
        pass

    return {
        "source": "api",
        "data": clean_data
    }