document.addEventListener("DOMContentLoaded", function() {
    const categories = [//'', 
    '1', '2', '3', '4', '5',
    ]
    categories.forEach(category => {
        const formattedStyle = category.replace(/ /g, ''); // Normalize the style name for use in IDs
        const chartId = `${formattedStyle}FreqGaugeChart`;
        const chartConfig = chartConfigsGauge[`freqChart${category}`]; // Assuming each style has its unique config
        const chartId2 = `${formattedStyle}CamGaugeChart`;
        const chartConfig2 = chartConfigsGauge[`camChart${category}`]; // Assuming each style has its unique config

        createChart(chartId, chartConfig, ''); // Empty title passed, replace with actual title if needed
        createChart(chartId2, chartConfig2, ''); // Empty title passed, replace with actual title if needed
    });

    function createChart(chartId, config, title) {
        const ctx = document.getElementById(chartId).getContext('2d');
        
        // text in the center
        const centerTextPlugin = {
            id: 'centerText',
            afterDraw: (chart) => {
                let ctx = chart.ctx;
                let height = chart.height;
                ctx.save();
                const centerX = (chart.chartArea.left + chart.chartArea.right) / 2;
                const centerY = (chart.chartArea.top + chart.chartArea.bottom) / 1.5;
                let fontSize = (height / 114).toFixed(2);
                ctx.font = fontSize + "em sans-serif";
                ctx.textAlign = 'center';
                ctx.textBaseline = 'middle';
                ctx.fillStyle = 'rgba(12, 12, 12, 1)';
                ctx.fillText(config.centerText, centerX, centerY);
                ctx.restore();
            }
        };

        new Chart(ctx, {
            type: 'doughnut',
            plugins: [centerTextPlugin],
            data: {
                labels: config.labels,
                datasets: [{
                    label: '% of total',
                    data: config.data,
                    backgroundColor: config.backgroundColor,
                    borderColor: config.borderColor,
                    borderWidth: 1,
                    circumference: 180,
                    rotation: 270
                }]
            },
            options: {
                plugins: {
                    legend: {display: false},
                    title: {display: false, text: config.title, 
                        padding: {bottom:-20, top: 10},
                        font: {
                            size: 18,  // Sets the font size to 24 pixels
                            style: 'bold',  // Optional: Makes the title bold
                        }                   
                    },
                    tooltip: { enabled: false }
                },
                responsive: true,
            }
        });
    }
});
