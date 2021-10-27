import "./App.css";
import mockPlantData from "./data/mockPlantData.js";
import React from "react";
import dataAnalyticsPage from "./pages/dataAnalytics.js";
import { BrowserRouter as Router, Route, Link } from "react-router-dom";
import stateSelection from "./components/stateSelecction";

function App() {
  return (
    <div className="App">
      <Router>
        <header className="App-header">
          <Route exact path="/">
            <h1>Home Page</h1>
            {stateSelection()}
            <br></br>
            <button>
              <Link to="/dataAnalytics">See the analytics</Link>
            </button>
          </Route>
          <Route path="/dataAnalytics">
            {dataAnalyticsPage(mockPlantData)}
          </Route>
        </header>
      </Router>
    </div>
  );
}

export default App;
