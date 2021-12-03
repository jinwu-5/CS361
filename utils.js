const { PythonShell } = require("python-shell");
const fs = require("fs");

async function writeToCSVFile(request, attack_request, forest_request) {
  // write service request in csv format based on the request state reveived
  fs.writeFile(attack_request, extractAsCSV(request), (err) => {
    if (err) {
      console.log("Error writing to csv file", err);
    }
  });
  fs.writeFile(forest_request, extractAsCSV(request), (err) => {
    if (err) {
      console.log("Error writing to csv file", err);
    }
  });
}

function extractAsCSV(request) {
  return request.join(", ");
}

function wait(ms) {
  return new Promise((r) => setTimeout(r, ms));
}

async function runServicePythonScript(attack_service, forest_service) {
  //run python script
  await wait(50);
  PythonShell.run(attack_service, null, function (err, result) {
    if (err) {
      console.log("Error running python script", err);
    }
  });
  PythonShell.run(forest_service, null, function (err, result) {
    if (err) {
      console.log("Error running python script", err);
    }
  });
}

const readServiceResponse = async (service_response) => {
  // read the service response csv file and return its content
  await wait(700);
  const fileContent = await new Promise((resolve, reject) => {
    return fs.readFile(service_response, "utf8", (err, data) => {
      if (err) {
        return reject(err);
      }
      return resolve(data);
    });
  });
  return fileContent;
};

module.exports = {
  writeToCSVFile,
  runServicePythonScript,
  readServiceResponse,
  wait,
};
