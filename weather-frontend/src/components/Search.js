import "../App.css";
function Search({ city, setCity, fetchWeather }) {
  return (
    <div>
      <input
        type="text"
        placeholder="Buscar ciudad..."
        value={city}
        onChange={(e) => setCity(e.target.value)}
      />

      <button onClick={fetchWeather}>Buscar</button>
    </div>
  );
}

export default Search;