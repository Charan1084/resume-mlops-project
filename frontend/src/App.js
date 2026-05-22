import { useState } from "react";

function App() {
  const [experience, setExperience] = useState("");
  const [skills, setSkills] = useState("");
  const [projects, setProjects] = useState("");
  const [result, setResult] = useState("");
  const [loading, setLoading] = useState(false);

  const handlePredict = async () => {
    setLoading(true);
    setResult("");

    try {
      const response = await fetch("http://127.0.0.1:8000/predict", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          experience: Number(experience),
          skills: Number(skills),
          projects: Number(projects),
        }),
      });

      const data = await response.json();
      setResult(data.prediction);
    } catch (error) {
      setResult("Error connecting to backend");
    }

    setLoading(false);
  };

  return (
    <div style={{ padding: "40px", fontFamily: "Arial" }}>
      <h1>1 Resume Shortlisting MLOps System</h1>

      <div style={{ marginTop: "20px" }}>
        <input
          placeholder="Experience"
          value={experience}
          onChange={(e) => setExperience(e.target.value)}
          style={{ margin: "5px", padding: "8px" }}
        />
        <br />

        <input
          placeholder="Skills"
          value={skills}
          onChange={(e) => setSkills(e.target.value)}
          style={{ margin: "5px", padding: "8px" }}
        />
        <br />

        <input
          placeholder="Projects"
          value={projects}
          onChange={(e) => setProjects(e.target.value)}
          style={{ margin: "5px", padding: "8px" }}
        />
        <br /><br />

        <button
          onClick={handlePredict}
          style={{
            padding: "10px 20px",
            cursor: "pointer",
            backgroundColor: "#4CAF50",
            color: "white",
            border: "none",
          }}
        >
          Predict
        </button>

        {loading && <p>Processing...</p>}

        <h2 style={{ marginTop: "20px" }}>
          Result: {result}
        </h2>
      </div>
    </div>
  );
}

export default App;