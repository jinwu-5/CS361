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
const fs = require("fs");

app.get("/analytics", (req, res) => {
  const request = ["State", req.query.states];
  const filename = "attack_request.csv";
  console.log(request);
  async function writeToCSVFile(request) {
    fs.writeFile(filename, extractAsCSV(request), (err) => {
      if (err) {
        console.log("Error writing to csv file", err);
      } else {
        console.log("2nd call", extractAsCSV(request));
        console.log(`saved as ${filename}`);
      }
    });
  }

  function extractAsCSV(request) {
    return request.join(", ");
  }

  function wait(ms) {
    return new Promise((r) => setTimeout(r, ms));
  }

  async function runAttackServicePythonScript() {
    await wait(50);
    PythonShell.run("attack_service.py", null, function (err, result) {});
    console.log("3rd call", "python ran");
  }

  async function readAttackServiceResponse() {
    await wait(400);
    fs.readFile("attack_response.csv", "utf8", (err, data) => {
      if (err) return console.error("Error while opening file");
      attackResponse = String(data).split(", ");
      console.log("4th call", "send data");
      res.send(
        "Hi there, here is " +
          attackResponse[0] +
          ", the chance of bear attack is " +
          attackResponse[1] +
          "%, which is " +
          attackResponse[2] +
          "."
      );
    });
  }

  function runPipeline() {
    writeToCSVFile(request);
    runAttackServicePythonScript();
    readAttackServiceResponse();
  }
  runPipeline();
});

app.listen(PORT, () => {
  console.log(`Server listening on port ${PORT}...`);
});
