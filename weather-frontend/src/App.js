import { useState } from "react";
import "./App.css";
import Search from "./components/Search";
import WeatherCard from "./components/WeatherCard";
import HourlyList from "./components/HourlyList";

function App() {
  const [city, setCity] = useState("")
  const [weather, setWeather] = useState(null)
  const [loading, setLoading] = useState(false)

  const fetchWeather = async () => {
    if (!city) return

    setLoading(true)

    const res = await fetch(`http://localhost:8000/weather?city=${city}`)
    const data = await res.json()

    setWeather(data.data)
    setLoading(false)
  }
  
  return (
    <div className="app-container" style={{padding: "20px"}}>
      <h1>Weather App</h1>

      <Search city={city} setCity={setCity} fetchWeather={fetchWeather}/>
      <button onClick={fetchWeather}>Refrescar</button>

      {loading && <p>Cargando...</p>}

      {weather && (
        <>
          <WeatherCard weather= {weather}/>
          <HourlyList hourly= {weather.hourly}/>
        </>
      )}
    </div>
  )
}

export default App;
