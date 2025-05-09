import React, { useEffect, useState } from 'react';

function App() {
  const [message, setMessage] = useState("Connecting to backend...");

  useEffect(() => {
    fetch('http://localhost:5000/api/test') // Backend must be running on port 5000
      .then(res => res.json())
      .then(data => {
        console.log("✅ Backend says:", data.message);
        setMessage(data.message);
      })
      .catch(err => {
        console.error("❌ Error connecting to backend:", err);
        setMessage("❌ Could not connect to backend");
      });
  }, []);

  return (
    <div style={{ padding: '2rem', fontFamily: 'Arial' }}>
      <h1>Flood Evacuation App</h1>
      <p>Status: {message}</p>
    </div>
  );
}

export default App;
