// HORIZONTAL BAR CHART
document.addEventListener("DOMContentLoaded", function() {
    const ctx = document.getElementById('myChart').getContext('2d');
    const myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: chartConfig.labels,
            datasets: [{
                label: '% of total',
                data: chartConfig.dataValues,
                backgroundColor: chartConfig.backgroundColor,
                borderColor: chartConfig.borderColor,
                borderWidth: 1
            }]
        },
        options: {
            indexAxis: 'y',
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        font: {
                            family: 'Montserrat', // Set font family to Montserrat
                            weight: 'bold', // Make y-axis labels bold
                            size: 16
                        }
                    }
                },
                x: {
                    ticks: {
                        font: {
                            family: 'Montserrat', // Set font family to Montserrat
                            weight: 'bold', // Make y-axis labels bold
                            size: 16
                        }
                    }
                }
            },
            plugins: {
                legend: {display: false},
                title: { display: false,  },
            }
        }
    });
});
