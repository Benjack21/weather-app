# 🌦️ Weather App (Fullstack)

Aplicación fullstack de clima que permite consultar el estado actual y las próximas 24 horas para una ciudad, utilizando una API externa, caché con Redis y un frontend en React.

---

## 🚀 Características

* Búsqueda de clima por ciudad
* Visualización de:

  * Temperatura actual
  * Descripción del clima
  * Velocidad del viento
  * Probabilidad de lluvia
* Pronóstico de las próximas 24 horas
* Sistema de caché con Redis (expiración de 12 horas)
* Integración con API externa (Visual Crossing)
* Arquitectura cliente-servidor (React + FastAPI)

---

## 🧱 Tecnologías utilizadas

### Backend

* Python
* FastAPI
* Redis
* Requests

### Frontend

* React
* JavaScript (ES6)
* CSS

---

## ⚙️ Instalación

### 1. Clonar repositorio

```bash
git clone https://github.com/tu-usuario/weather-app.git
cd weather-app
```

---

## 🔙 Backend setup

### Crear entorno virtual

```bash
python -m venv venv
venv\Scripts\activate
```

### Instalar dependencias

```bash
pip install -r requirements.txt
```

### Configurar variables de entorno

Crear archivo `.env`:

```env
WEATHER_API_KEY=tu_api_key
WEATHER_API_URL=https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline
REDIS_URL=redis://localhost:6379
```

### Ejecutar servidor

```bash
uvicorn app.main:app --reload
```

Servidor disponible en:

```
http://localhost:8000
```

---

## 🔜 Frontend setup

```bash
cd weather-frontend
npm install
npm start
```

App disponible en:

```
http://localhost:3000
```

---

## 🔄 Uso

1. Ingresar una ciudad (ej: Santiago)
2. Presionar "Buscar"
3. Visualizar:

   * Clima actual
   * Datos adicionales
   * Pronóstico por hora
4. Usar botón "Refrescar" para actualizar datos

---

## 🧠 Arquitectura

```
Frontend (React)
        ↓
Backend (FastAPI)
        ↓
API externa (Visual Crossing)
        ↓
Redis (caché)
```

---

## ⚠️ Manejo de errores

* 400 → Ciudad inválida
* 502 → API externa no disponible
* 500 → Error interno

---

## 📦 Ejemplo de respuesta

```json
{
  "source": "api",
  "data": {
    "city": "Santiago",
    "temperature": 20.4,
    "description": "Parcialmente nublado",
    "wind_speed": 24.1,
    "rain_probability": 0,
    "hourly": [
      {
        "time": "10:00",
        "temperature": 18,
        "conditions": "Partially cloudy"
      }
    ]
  }
}
```

---

## 📌 Estado del proyecto

✔ Funcional
✔ Integración completa backend/frontend
✔ Uso de caché
✔ Listo para portafolio

---

## 👨‍💻 Autor

Desarrollado por [Benjamin Caceres]

---
