import { BrowserRouter, Routes, Route } from "react-router-dom";

import Dashboard from "../pages/Dashboard/Dashboard";
import LogInteraction from "../pages/LogInteraction/LogInteraction";
import AIAssistant from "../pages/AIAssistant/AIAssistant";

function AppRoutes() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/log-interaction" element={<LogInteraction />} />
        <Route path="/assistant" element={<AIAssistant />} />
      </Routes>
    </BrowserRouter>
  );
}

export default AppRoutes;