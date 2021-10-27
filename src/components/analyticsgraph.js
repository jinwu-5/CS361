import { Bar } from "react-chartjs-2";
import mockPlantData from "../data/mockPlantData";

function analyticsGraph() {
  return (
    <div className="App">
      <h1>Data Analytics</h1>
      <div style={{ maxWidth: "650px" }}>
        <Bar
          data={{
            labels: ["plant_1", "plant_2", "plant_3", "plant_4"],
            datasets: [
              {
                label: "plant populations and # of bear attacks for Oregon",
                data: mockPlantData,
                backgroundColor: ["purple", "green", "orange", "yellow"],
                borderColor: ["purple", "green", "orange", "yellow"],
                borderWidth: 0.5,
              },
            ],
          }}
          height={400}
          options={{
            maintainAspectRatio: false,
            scales: {
              yAxes: [
                {
                  ticks: {
                    beginAtZero: true,
                  },
                },
              ],
            },
            legend: {
              labels: {
                fontSize: 15,
              },
            },
          }}
        />
      </div>
    </div>
  );
}

export default analyticsGraph;
