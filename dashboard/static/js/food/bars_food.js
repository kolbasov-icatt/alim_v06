document.addEventListener("DOMContentLoaded", function() {
    function createChart(chartId, config) {
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
                    title: {display: false, text: title},
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

    createChart('FreqChartCountries', chartConfigsBars.freqChartCountries);
    createChart('FreqChartGenerations', chartConfigsBars.freqChartGenerations);
    createChart('FreqChartStyles', chartConfigsBars.freqChartStyles);

    
});
