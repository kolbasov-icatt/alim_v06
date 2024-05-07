const centerTextPlugin = {
    id: 'centerText',
    afterDraw: (chart) => {
        let ctx = chart.ctx;
        ctx.save();
        const centerX = (chart.chartArea.left + chart.chartArea.right) / 2;
        const centerY = (chart.chartArea.top + chart.chartArea.bottom) / 1.5;
        ctx.font = '20px Arial';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillStyle = 'rgba(12, 12, 12, 1)';
        const value = Number(food1_freq.toFixed(1));
        ctx.fillText(value, centerX, centerY);
        ctx.restore();
    }
};

const centerTextPluginCam = {
    id: 'centerTextCam',
    afterDraw: (chart) => {
        let ctx = chart.ctx;
        ctx.save();
        const centerX = (chart.chartArea.left + chart.chartArea.right) / 2;
        const centerY = (chart.chartArea.top + chart.chartArea.bottom) / 1.5;
        ctx.font = '20px Arial';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillStyle = 'rgba(12, 12, 12, 1)';
        const value = Number(food1_cam.toFixed(0));
        ctx.fillText(value + '%', centerX, centerY);
        ctx.restore();
    }
};

const gaugeData = {
    labels: [food1_label, ''],
    datasets: [{
        data: [food1_freq, 20 - food1_freq],
        backgroundColor: [country.color, country.color_empty],
        borderColor: [country.border_color, country.border_color_empty],
        borderWidth: 1,
        circumference: 180,
        rotation: 270
    }]
};

const gaugeDataCam = {
    labels: [food1_cam + '%', ''],
    datasets: [{
        data: [(food1_cam + 100) / 2, 100 - ((food1_cam + 100) / 2)],
        backgroundColor: [country.color2, country.color_empty2],
        borderColor: [country.border_color2, country.border_color_empty2],
        borderWidth: 1,
        circumference: 180,
        rotation: 270
    }]
};

const ctxGauge = document.getElementById('doughnutChart').getContext('2d');
const gaugeChart = new Chart(ctxGauge, {
    type: 'doughnut',
    data: gaugeData,
    options: {
        cutout: '50%',
        plugins: {
            legend: { display: false },
            title: { display: true, text: 'Frequenza (Media giorni/mese)' },
            tooltip: { enabled: false }
        }
    },
    plugins: [centerTextPlugin]
});

const ctxGaugeCam = document.getElementById('doughnutChartCam').getContext('2d');
const gaugeChartCam = new Chart(ctxGaugeCam, {
    type: 'doughnut',
    data: gaugeDataCam,
    options: {
        cutout: '50%',
        plugins: {
            legend: { display: false },
            title: { display: true, text: 'Cambiamento' },
            tooltip: { enabled: false }
        },
        animation: {
            animateRotate: true
        }
    },
    plugins: [centerTextPluginCam]
});

// THE SECOND FOOD
const centerTextPlugin2 = {
    id: 'centerText',
    afterDraw: (chart) => {
        let ctx = chart.ctx;
        ctx.save();
        const centerX = (chart.chartArea.left + chart.chartArea.right) / 2;
        const centerY = (chart.chartArea.top + chart.chartArea.bottom) / 1.5;
        ctx.font = '20px Arial';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillStyle = 'rgba(12, 12, 12, 1)';
        const value = Number(food2_freq.toFixed(1));
        ctx.fillText(value, centerX, centerY);
        ctx.restore();
    }
};

const centerTextPluginCam2 = {
    id: 'centerTextCam',
    afterDraw: (chart) => {
        let ctx = chart.ctx;
        ctx.save();
        const centerX = (chart.chartArea.left + chart.chartArea.right) / 2;
        const centerY = (chart.chartArea.top + chart.chartArea.bottom) / 1.5;
        ctx.font = '20px Arial';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillStyle = 'rgba(12, 12, 12, 1)';
        const value = Number(food2_cam.toFixed(0));
        ctx.fillText(value + '%', centerX, centerY);
        ctx.restore();
    }
};

const gaugeData2 = {
    labels: [food2_label, ''],
    datasets: [{
        data: [food2_freq, 20 - food2_freq],
        backgroundColor: [country.color, country.color_empty],
        borderColor: [country.border_color, country.border_color_empty],
        borderWidth: 1,
        circumference: 180,
        rotation: 270
    }]
};

const gaugeDataCam2 = {
    labels: [food2_cam + '%', ''],
    datasets: [{
        data: [(food2_cam + 100) / 2, 100 - ((food2_cam + 100) / 2)],
        backgroundColor: [country.color2, country.color_empty2],
        borderColor: [country.border_color2, country.border_color_empty2],
        borderWidth: 1,
        circumference: 180,
        rotation: 270
    }]
};

const ctxGauge2 = document.getElementById('doughnutChart2').getContext('2d');
const gaugeChart2 = new Chart(ctxGauge2, {
    type: 'doughnut',
    data: gaugeData2,
    options: {
        cutout: '50%',
        plugins: {
            legend: { display: false },
            title: { display: true, text: 'Frequenza (Media giorni/mese)' },
            tooltip: { enabled: false }
        }
    },
    plugins: [centerTextPlugin2]
});

const ctxGaugeCam2 = document.getElementById('doughnutChartCam2').getContext('2d');
const gaugeChartCam2 = new Chart(ctxGaugeCam2, {
    type: 'doughnut',
    data: gaugeDataCam2,
    options: {
        cutout: '50%',
        plugins: {
            legend: { display: false },
            title: { display: true, text: 'Cambiamento' },
            tooltip: { enabled: false }
        },
        animation: {
            animateRotate: true
        }
    },
    plugins: [centerTextPluginCam2]
});

// THE 3 FOOD
const centerTextPlugin3 = {
    id: 'centerText',
    afterDraw: (chart) => {
        let ctx = chart.ctx;
        ctx.save();
        const centerX = (chart.chartArea.left + chart.chartArea.right) / 2;
        const centerY = (chart.chartArea.top + chart.chartArea.bottom) / 1.5;
        ctx.font = '20px Arial';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillStyle = 'rgba(12, 12, 12, 1)';
        const value = Number(food3_freq.toFixed(1));
        ctx.fillText(value, centerX, centerY);
        ctx.restore();
    }
};

const centerTextPluginCam3 = {
    id: 'centerTextCam',
    afterDraw: (chart) => {
        let ctx = chart.ctx;
        ctx.save();
        const centerX = (chart.chartArea.left + chart.chartArea.right) / 2;
        const centerY = (chart.chartArea.top + chart.chartArea.bottom) / 1.5;
        ctx.font = '20px Arial';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillStyle = 'rgba(12, 12, 12, 1)';
        const value = Number(food3_cam.toFixed(0));
        ctx.fillText(value + '%', centerX, centerY);
        ctx.restore();
    }
};

const gaugeData3 = {
    labels: [food3_label, ''],
    datasets: [{
        data: [food3_freq, 20 - food3_freq],
        backgroundColor: [country.color, country.color_empty],
        borderColor: [country.border_color, country.border_color_empty],
        borderWidth: 1,
        circumference: 180,
        rotation: 270
    }]
};

const gaugeDataCam3 = {
    labels: [food3_cam + '%', ''],
    datasets: [{
        data: [(food3_cam + 100) / 2, 100 - ((food3_cam + 100) / 2)],
        backgroundColor: [country.color2, country.color_empty2],
        borderColor: [country.border_color2, country.border_color_empty2],
        borderWidth: 1,
        circumference: 180,
        rotation: 270
    }]
};

const ctxGauge3 = document.getElementById('doughnutChart3').getContext('2d');
const gaugeChart3 = new Chart(ctxGauge3, {
    type: 'doughnut',
    data: gaugeData3,
    options: {
        cutout: '50%',
        plugins: {
            legend: { display: false },
            title: { display: true, text: 'Frequenza (Media giorni/mese)' },
            tooltip: { enabled: false }
        }
    },
    plugins: [centerTextPlugin3]
});

const ctxGaugeCam3 = document.getElementById('doughnutChartCam3').getContext('2d');
const gaugeChartCam3 = new Chart(ctxGaugeCam3, {
    type: 'doughnut',
    data: gaugeDataCam3,
    options: {
        cutout: '50%',
        plugins: {
            legend: { display: false },
            title: { display: true, text: 'Cambiamento' },
            tooltip: { enabled: false }
        },
        animation: {
            animateRotate: true
        }
    },
    plugins: [centerTextPluginCam3]
});

// THE 4 FOOD
const centerTextPlugin4 = {
    id: 'centerText',
    afterDraw: (chart) => {
        let ctx = chart.ctx;
        ctx.save();
        const centerX = (chart.chartArea.left + chart.chartArea.right) / 2;
        const centerY = (chart.chartArea.top + chart.chartArea.bottom) / 1.5;
        ctx.font = '20px Arial';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillStyle = 'rgba(12, 12, 12, 1)';
        const value = Number(food4_freq.toFixed(1));
        ctx.fillText(value, centerX, centerY);
        ctx.restore();
    }
};

const centerTextPluginCam4 = {
    id: 'centerTextCam',
    afterDraw: (chart) => {
        let ctx = chart.ctx;
        ctx.save();
        const centerX = (chart.chartArea.left + chart.chartArea.right) / 2;
        const centerY = (chart.chartArea.top + chart.chartArea.bottom) / 1.5;
        ctx.font = '20px Arial';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillStyle = 'rgba(12, 12, 12, 1)';
        const value = Number(food4_cam.toFixed(0));
        ctx.fillText(value + '%', centerX, centerY);
        ctx.restore();
    }
};

const gaugeData4 = {
    labels: [food4_label, ''],
    datasets: [{
        data: [food4_freq, 20 - food4_freq],
        backgroundColor: [country.color, country.color_empty],
        borderColor: [country.border_color, country.border_color_empty],
        borderWidth: 1,
        circumference: 180,
        rotation: 270
    }]
};

const gaugeDataCam4 = {
    labels: [food4_cam + '%', ''],
    datasets: [{
        data: [(food4_cam + 100) / 2, 100 - ((food4_cam + 100) / 2)],
        backgroundColor: [country.color2, country.color_empty2],
        borderColor: [country.border_color2, country.border_color_empty2],
        borderWidth: 1,
        circumference: 180,
        rotation: 270
    }]
};

const ctxGauge4 = document.getElementById('doughnutChart4').getContext('2d');
const gaugeChart4 = new Chart(ctxGauge4, {
    type: 'doughnut',
    data: gaugeData4,
    options: {
        cutout: '50%',
        plugins: {
            legend: { display: false },
            title: { display: true, text: 'Frequenza (Media giorni/mese)' },
            tooltip: { enabled: false }
        }
    },
    plugins: [centerTextPlugin4]
});

const ctxGaugeCam4 = document.getElementById('doughnutChartCam4').getContext('2d');
const gaugeChartCam4 = new Chart(ctxGaugeCam4, {
    type: 'doughnut',
    data: gaugeDataCam4,
    options: {
        cutout: '50%',
        plugins: {
            legend: { display: false },
            title: { display: true, text: 'Cambiamento' },
            tooltip: { enabled: false }
        },
        animation: {
            animateRotate: true
        }
    },
    plugins: [centerTextPluginCam4]
});

// THE 3 FOOD
const centerTextPlugin5 = {
    id: 'centerText',
    afterDraw: (chart) => {
        let ctx = chart.ctx;
        ctx.save();
        const centerX = (chart.chartArea.left + chart.chartArea.right) / 2;
        const centerY = (chart.chartArea.top + chart.chartArea.bottom) / 1.5;
        ctx.font = '20px Arial';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillStyle = 'rgba(12, 12, 12, 1)';
        const value = Number(food5_freq.toFixed(1));
        ctx.fillText(value, centerX, centerY);
        ctx.restore();
    }
};

const centerTextPluginCam5 = {
    id: 'centerTextCam',
    afterDraw: (chart) => {
        let ctx = chart.ctx;
        ctx.save();
        const centerX = (chart.chartArea.left + chart.chartArea.right) / 2;
        const centerY = (chart.chartArea.top + chart.chartArea.bottom) / 1.5;
        ctx.font = '20px Arial';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillStyle = 'rgba(12, 12, 12, 1)';
        const value = Number(food5_cam.toFixed(0));
        ctx.fillText(value + '%', centerX, centerY);
        ctx.restore();
    }
};

const gaugeData5 = {
    labels: [food5_label, ''],
    datasets: [{
        data: [food5_freq, 20 - food5_freq],
        backgroundColor: [country.color, country.color_empty],
        borderColor: [country.border_color, country.border_color_empty],
        borderWidth: 1,
        circumference: 180,
        rotation: 270
    }]
};

const gaugeDataCam5 = {
    labels: [food5_cam + '%', ''],
    datasets: [{
        data: [(food5_cam + 100) / 2, 100 - ((food5_cam + 100) / 2)],
        backgroundColor: [country.color2, country.color_empty2],
        borderColor: [country.border_color2, country.border_color_empty2],
        borderWidth: 1,
        circumference: 180,
        rotation: 270
    }]
};

const ctxGauge5 = document.getElementById('doughnutChart5').getContext('2d');
const gaugeChart5 = new Chart(ctxGauge5, {
    type: 'doughnut',
    data: gaugeData5,
    options: {
        cutout: '50%',
        plugins: {
            legend: { display: false },
            title: { display: true, text: 'Frequenza (Media giorni/mese)' },
            tooltip: { enabled: false }
        }
    },
    plugins: [centerTextPlugin5]
});

const ctxGaugeCam5 = document.getElementById('doughnutChartCam5').getContext('2d');
const gaugeChartCam5 = new Chart(ctxGaugeCam5, {
    type: 'doughnut',
    data: gaugeDataCam5,
    options: {
        cutout: '50%',
        plugins: {
            legend: { display: false },
            title: { display: true, text: 'Cambiamento' },
            tooltip: { enabled: false }
        },
        animation: {
            animateRotate: true
        }
    },
    plugins: [centerTextPluginCam5]
});