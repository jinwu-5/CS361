import React from "react";
import { Link } from "react-router-dom";
import analyticsGraph from "../components/analyticsGraph";

const dataAnalyticsPage = (props) => {
  return (
    <>
      {analyticsGraph()}
      <br></br>
      <img src="/bear.JPG" alt="bear" width="100" height="100" />
      <h4> # of bear attack: 66</h4>
      <br></br>
      <Link to="/"> Go to the Home Page</Link>
    </>
  );
};

export default dataAnalyticsPage;
