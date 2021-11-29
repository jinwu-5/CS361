const PORT = process.env.PORT || 3000;

const {
  writeToCSVFile,
  runServicePythonScript,
  readServiceResponse,
} = require("./utils.js");

const express = require("express");
const app = express();

// Handlebars Setup
var exphbs = require("express-handlebars");
app.engine(
  ".hbs",
  exphbs({
    extname: ".hbs",
  })
);
app.set("view engine", ".hbs");

app.use(express.static("public"));

app.use(
  express.urlencoded({
    extended: true,
  })
);

app.use(express.json());

/**
 * Routes
 */

// Homepage
app.get("/", (req, res) => {
  res.render("home");
});

app.get("/home", (req, res) => {
  res.render("home");
});

// Analytics
app.get("/analytics", (req, res) => {
  const request = ["State", req.query.states];

  let attackData, forestData, combineData;

  writeToCSVFile(request, "attack_request.csv", "forest_request.csv")
    .then(() => {
      runServicePythonScript("attack_service.py", "forest_service.py");
    })
    .then(() =>
      readServiceResponse("attack_response.csv")
        .then((data) => {
          attackData = data;
        })
        .then(() => readServiceResponse("forest_response.csv"))
        .then((data) => {
          forestData = data;
          combineData = attackData + ", " + forestData;
          combineData = String(combineData).split(", ");

          // remove brackets from the string

          for (i = 1; i < combineData.length; i++) {
            combineData[i] = combineData[i].replace(/[\[\]']+/g, "");
          }

          let dataObject = {
            state: combineData[0],
            attackRisk: combineData[1],
            chanceOfAttack: combineData[2],
            forestCoverage: combineData[4],
            redMaple: combineData[5],
            loblollyPine: combineData[6],
            mapleSugar: combineData[7],
            floweringDogwood: combineData[8],
          };

          res.render("analytics", { data: dataObject });
        })
    );
});

app.listen(PORT, () => {
  console.log(`Server listening on port ${PORT}...`);
});
