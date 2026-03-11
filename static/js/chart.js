const ctx = document.getElementById("defectChart");

if (ctx) {

new Chart(ctx, {
    type: "bar",
    data: {
        labels: ["Engine","Hydraulics","Avionics","Landing Gear"],
        datasets: [{
            label: "Reported Defects",
            data: [5,3,4,2],
            backgroundColor: [
                "#4cc9f0",
                "#4361ee",
                "#f72585",
                "#fca311"
            ]
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            legend: {
                labels: {
                    color: "white"
                }
            }
        },
        scales: {
            x: {
                ticks: {
                    color: "white"
                }
            },
            y: {
                ticks: {
                    color: "white"
                }
            }
        }
    }
});

}