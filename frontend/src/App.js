import { useEffect, useState } from "react";
import "./App.css";

const ENDPOINT = process.env.REACT_APP_ENDPOINT;

function App() {
  const [todayAlarm, setTodayAlarm] = useState("");
  const [tomorrowAlarm, setTomorrowAlarm] = useState("");

  useEffect(() => {
    var tomorrow = new Date();
    tomorrow.setDate(new Date().getDate() + 1);

    fetch(ENDPOINT)
      .then((response) => response.json())
      .then((data) => setTodayAlarm(data));

    fetch(ENDPOINT, {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        context: {
          year: tomorrow.getFullYear(),
          month: tomorrow.getMonth() + 1,
          day: tomorrow.getDate(),
          hour: 0,
          minute: 1,
        },
      }),
    })
      .then((response) => response.json())
      .then((data) => setTomorrowAlarm(data));
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <p>Today's alarm</p>
        <p>{JSON.stringify(todayAlarm)}</p>
        <p>Tomorrow</p>
        <p>{JSON.stringify(tomorrowAlarm)}</p>
      </header>
    </div>
  );
}

export default App;
