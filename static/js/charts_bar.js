document.addEventListener("DOMContentLoaded", function() {
    function createChart(chartId, config, title) {
        const ctx = document.getElementById(chartId).getContext('2d');
        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: config.labels,
                datasets: [{
                    label: '% of total',
                    data: config.data,
                    backgroundColor: config.backgroundColor,
                    borderColor: config.borderColor,
                    borderWidth: 1
                }]
            },
            options: {
                plugins: {
                    legend: {display: false},
                    title: {display: true, text: title},
                },
                scales: {
                    y: { beginAtZero: true },
                    x: {
                        categoryPercentage: 1.0,
                        barPercentage: 1
                    }
                },
            }
        });
    }

    createChart('GenderChart', chartConfigs.genderChart, 'Genere');
    createChart('RespChart', chartConfigs.respChart, 'Responsabili acquisti');
    createChart('GenerationChart', chartConfigs.generationChart, 'Gnerazioni');
    createChart('AreaChart', chartConfigs.areaChart, 'Area');
});
