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
                                //weight: 'bold', 
                                size: 16
                            }
                        }
                    }
                },
            }
        });
    }
    createChart('FS_Countries', chartConfigsBars.FS_Countries);
    createChart('FS_Areas', chartConfigsBars.FS_Areas);
    createChart('FS_Generations', chartConfigsBars.FS_Generations);
    createChart('FS_Genders', chartConfigsBars.FS_Genders);       
});
