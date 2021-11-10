// MyStuff.js
/* global localStorage */

// Use localStorage below with no linter errors

const PORT = process.env.PORT || 3000;

const express = require("express");

const app = express();

app.use(
  express.urlencoded({
    extended: true,
  })
);

app.use(express.static("public"));

let { PythonShell } = require("python-shell");

app.get("/analytics", (req, res) => {
  PythonShell.run("forest_service.py", null, function (err, result) {});
});

app.listen(PORT, () => {
  console.log(`Server listening on port ${PORT}...`);
});
