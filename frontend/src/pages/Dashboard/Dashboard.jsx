import { useEffect, useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import api from "../../api/api";

function Dashboard() {

    const [interactions, setInteractions] = useState([]);
    const navigate = useNavigate();

    useEffect(() => {
        loadInteractions();
    }, []);

    const loadInteractions = async () => {
        try {
            const response = await api.get("/interactions/");
            setInteractions(response.data);
        } catch (err) {
            console.log(err);
        }
    };

    return (

        <div style={{ padding: "40px" }}>

            <h1>AI CRM HCP Dashboard</h1>

            <p>Manage Healthcare Professional interactions.</p>

            <div style={{ marginBottom: "20px" }}>

                <Link to="/log-interaction">
                    <button style={{ marginRight: "10px" }}>
                        Log New Interaction
                    </button>
                </Link>

                <button onClick={() => navigate("/assistant")}>
                    AI Assistant
                </button>

            </div>

            <hr />

            <h2>Recent Interactions</h2>

            <table
                border="1"
                cellPadding="10"
                style={{
                    width: "100%",
                    borderCollapse: "collapse"
                }}
            >

                <thead>

                    <tr>
                        <th>ID</th>
                        <th>Date</th>
                        <th>Type</th>
                        <th>Topics</th>
                        <th>Summary</th>
                    </tr>

                </thead>

                <tbody>

                    {interactions.map((item) => (

                        <tr key={item.id}>

                            <td>{item.id}</td>

                            <td>{item.interaction_date}</td>

                            <td>{item.interaction_type}</td>

                            <td>{item.topics_discussed}</td>

                            <td>{item.summary}</td>

                        </tr>

                    ))}

                </tbody>

            </table>

        </div>

    );
}

export default Dashboard;