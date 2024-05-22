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
                    title: {display: false, text: title},
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
                                //weight: 'bold', 
                                size: 16
                            }
                        }
                    }
                },
            }
        });
    }
    createChart('StiliChart', chartConfigs.stiliChart, '');
    createChart('GenderChart', chartConfigs.genderChart, 'Genere');
    //createChart('RespChart', chartConfigs.respChart, 'Responsabili acquisti');
    createChart('GenerationChart', chartConfigs.generationChart, 'Gnerazioni');
    createChart('AreaChart', chartConfigs.areaChart, 'Area');
});
