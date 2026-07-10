import { useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../../api/api";
import "./LogInteraction.css";

function LogInteraction() {

  const navigate = useNavigate();

  const [conversation, setConversation] = useState("");

  const [formData, setFormData] = useState({
    hcp_id: 1,
    interaction_date: "",
    interaction_time: "",
    interaction_type: "",
    attendees: "",
    topics_discussed: "",
    summary: "",
    sentiment: "",
    outcomes: "",
    follow_up: "",
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const generateSummary = async () => {
  try {
    const response = await api.post("/ai/chat", {
      tool: "summary",
      message: conversation,
    });

    setFormData({
      ...formData,
      summary: response.data.response,
    });

  } catch (error) {
    console.log(error);
    alert("AI Summary Failed");
  }
};

const generateFollowup = async () => {
  try {
    const response = await api.post("/ai/chat", {
      tool: "followup",
      message: conversation,
    });

    setFormData({
      ...formData,
      follow_up: response.data.response,
    });

  } catch (error) {
    console.log(error);
    alert("AI Follow-up Failed");
  }
};

const saveInteraction = async () => {
  try {
    await api.post("/interactions/", formData);

    alert("Interaction Saved Successfully!");
    navigate("/");

  } catch (error) {
    console.log(error);
    alert("Failed to Save Interaction");
  }
};




return (

<div className="container">

<div className="card">

<h1>Log HCP Interaction</h1>

<label>Conversation</label>

<textarea
rows="6"
placeholder="Paste doctor's conversation..."
value={conversation}
onChange={(e)=>setConversation(e.target.value)}
/>

<button onClick={generateSummary}>
Generate AI Summary
</button>

<button onClick={generateFollowup}>
Generate Follow Up
</button>

<div className="grid">

<div>

<label>HCP ID</label>

<input
type="number"
name="hcp_id"
value={formData.hcp_id}
onChange={handleChange}
/>

<label>Date</label>

<input
type="date"
name="interaction_date"
value={formData.interaction_date}
onChange={handleChange}
/>

<label>Time</label>

<input
type="time"
name="interaction_time"
value={formData.interaction_time}
onChange={handleChange}
/>

<label>Interaction Type</label>

<input
type="text"
name="interaction_type"
value={formData.interaction_type}
onChange={handleChange}
/>

<label>Attendees</label>

<input
type="text"
name="attendees"
value={formData.attendees}
onChange={handleChange}
/>

<label>Topics Discussed</label>

<textarea
rows="4"
name="topics_discussed"
value={formData.topics_discussed}
onChange={handleChange}
/>

</div>

<div>

<label>AI Summary</label>

<textarea
rows="6"
name="summary"
value={formData.summary}
onChange={handleChange}
/>

<label>Sentiment</label>

<input
type="text"
name="sentiment"
value={formData.sentiment}
onChange={handleChange}
/>

<label>Outcomes</label>

<textarea
rows="4"
name="outcomes"
value={formData.outcomes}
onChange={handleChange}
/>

<label>Follow Up</label>

<textarea
rows="6"
name="follow_up"
value={formData.follow_up}
onChange={handleChange}
/>

</div>

</div>

<button onClick={saveInteraction}>
Save Interaction
</button>

</div>

</div>

);
}

export default LogInteraction;