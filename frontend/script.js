async function getPath() {
  const start = document.getElementById("start").value.trim();
  const end = document.getElementById("end").value.trim();
  const algo = document.getElementById("algo").value;

  if (!start || !end) {
    document.getElementById("output").innerText =
      "❌ Please enter both start and end nodes.";
    return;
  }

  try {
    const response = await fetch(`http://127.0.0.1:5000/${algo}`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ start, end }),
    });

    const data = await response.json();

    if (response.ok) {
      document.getElementById("output").innerText = `✅ Path: ${data.path.join(
        " → "
      )}\n🧭 Cost: ${data.distance}`;
    } else {
      document.getElementById("output").innerText = `⚠️ ${data.error}`;
    }
  } catch (err) {
    document.getElementById("output").innerText =
      "❌ Could not reach the backend server.";
    console.error(err);
  }
}
