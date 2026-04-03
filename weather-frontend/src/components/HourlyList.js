import "../App.css";
function HourlyList({ hourly }) {
  return (
    <div className="hourly-list">
      {hourly.map((h, index) => (
        <div className="hourly-item">
          <span>{h.time}</span>
          <span>{h.temperature}°C</span>
          <span>{h.conditions}</span>
        </div>
      ))}
    </div>
  );
}

export default HourlyList;