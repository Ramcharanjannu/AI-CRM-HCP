import { useState } from "react";
import api from "../../api/api";
import "./AIAssistant.css";

function AIAssistant() {

    const [tool, setTool] = useState("summary");
    const [message, setMessage] = useState("");
    const [response, setResponse] = useState("");

    const runTool = async () => {

        try{

            const res = await api.post("/ai/chat",{
                tool,
                message
            });

            setResponse(res.data.response);

        }

        catch(err){
            console.log(err);
            alert("Tool Failed");
        }

    }

    return(

        <div className="assistant-container">

            <div className="assistant-card">

                <h1>AI Assistant</h1>

                <p>
                    Test all LangGraph AI Tools from one place.
                </p>

                <label>Select Tool</label>

                <select
                    value={tool}
                    onChange={(e)=>setTool(e.target.value)}
                >

                    <option value="summary">Generate Summary</option>

                    <option value="followup">Recommend Follow-up</option>

                    <option value="search">Search HCP</option>

                    <option value="edit">Edit Interaction</option>

                    <option value="log">Log Interaction</option>

                </select>

                <label>Input</label>

                <textarea
                    rows="10"
                    value={message}
                    onChange={(e)=>setMessage(e.target.value)}
                    placeholder="Type your request here..."
                />

                <button onClick={runTool}>
                    Run Tool
                </button>

                <label>AI Response</label>

                <textarea
                    rows="10"
                    value={response}
                    readOnly
                />

            </div>

        </div>

    );

}

export default AIAssistant;