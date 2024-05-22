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
                indexAxis: 'y',
                plugins: {
                    legend: {display: false},
                    title: {display: false, text: config.title},
                    tooltip: {
                        callbacks: {
                            label: function(tooltipItem) {
                                return tooltipItem.dataset.label + ': ' + tooltipItem.raw.toFixed(0) + '%';
                            }
                        }
                    }
                },
                scales: {
                    y: { beginAtZero: true,
                        ticks: {
                            color: 'black',
                            font: {
                                family: 'Montserrat', 
                                //weight: 'bold', 
                                size: 16
                            }
                        }
                    },
                    x: {
                        categoryPercentage: 1.0,
                        barPercentage: 1,
                        ticks: {
                            color: 'black',
                            font: {
                                family: 'Montserrat', 
                                //weight: 'bold', // Make y-axis labels bold
                                size: 16
                            }
                        }
                    }
                },
            }
        });
    }

    createChart('FreqChart', chartConfigs.freqChart);
    createChart('CamChart', chartConfigs.camChart);
    createChart('CamChartCountries', chartConfigs.camChartCountries);
    createChart('CamChartGenerations', chartConfigs.camChartGenerations);
    createChart('CamChartStyles', chartConfigs.camChartStyles);

});
