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
                    title: {display: false, },
                    
                },
                scales: {
                    y: { beginAtZero: true,
                        color: 'black',
                        ticks: {
                            font: {
                                family: 'Montserrat', 
                                //weight: 'bold', 
                                size: 16
                            }
                        }
                     },
                    x: {
                        color: 'black',
                        categoryPercentage: 1.0,
                        barPercentage: 1,
                        ticks: {
                            font: {
                                family: 'Montserrat', 
                                //weight: 'bold', 
                                size: 16
                            }
                        }
                    }
                },
            }
        });
    }

    createChart('FreqChartCountries', chartConfigsBars.freqChartCountries);
    createChart('FreqChartGenerations', chartConfigsBars.freqChartGenerations);
    createChart('FreqChartStyles', chartConfigsBars.freqChartStyles);

    
});
