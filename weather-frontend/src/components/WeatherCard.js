import "../App.css";
function WeatherCard({ weather }) {
  return (
    <div className="card">
      <h2>{weather.city}</h2>

      <div className="main-temp">
        {weather.temperature}°C
      </div>

      <div className="description">
        {weather.description}
      </div>

      <div className="details">
        Viento: {weather.wind_speed} km/h | Lluvia: {weather.rain_probability}%
      </div>
    </div>
  );
}

export default WeatherCard;