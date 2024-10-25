const data = fetch('/api/data')
data.then(response => response.json())
.then(data => {
    const ctx = document.getElementById('myChart').getContext('2d'); 
    const line = new Chart(ctx, {
        type: 'line',
        data: {
            labels: data.labels,
            datasets: data.datasets
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    })
})

const data2 = fetch('/api/data')
data2.then(response => response.json())
.then(data => {
    const ctx = document.getElementById('myChart2').getContext('2d');
    const bar = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: data.labels,
            datasets: data.datasets
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    })
})

const data3 = fetch('/api/data')
data3.then(response => response.json())
.then(data => {
    const ctx = document.getElementById('myChart3').getContext('2d');
    const pie = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: data.labels,
            datasets: data.datasets
        }
    })
})

const data4 = fetch('/api/data')
data4.then(response => response.json())
.then(data => {
    const ctx = document.getElementById('myChart4').getContext('2d');
    const doughnut = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: data.labels,
            datasets: data.datasets
        }
    })
})

const data5 = fetch('/api/data')
data5.then(response => response.json())
.then(data => {
    const ctx = document.getElementById('myChart5').getContext('2d');
    const radar = new Chart(ctx, {
        type: 'radar',
        data: {
            labels: data.labels,
            datasets: data.datasets
        }
    })
})

const data6 = fetch('/api/data')
data6.then(response => response.json())
.then(data => {
    const ctx = document.getElementById('myChart6').getContext('2d');
    const polarArea = new Chart(ctx, {
        type: 'polarArea',
        data: {
            labels: data.labels,
            datasets: data.datasets
        }
    })
})



.catch(error => console.error('Error al cargar los datos', error));




// const areaChartData = {
//     labels      : ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio'],
//     datasets    : [
//         {
//             label               : 'Publicaciones Activas',
//             backgroundColor     : 'rgba(60,141,188,0.9)',
//             borderColor         : 'rgba(60,141,188,0.8)',
//             pointRadius         : false,
//             pointColor          : '#3b8bba',
//             pointStrokeColor    : 'rgba(60,141,188,1)',
//             pointHighlightFill  : '#fff',
//             pointHighlightStroke: 'rgba(60,141,188,1)',
//             data                : [28, 48, 40, 19, 86, 27, 90]
//         },
//         {
//             label               : 'Publicaciones Inactivas',
//             backgroundColor     : 'rgba(210, 214, 222, 1)',
//             borderColor         : 'rgba(210, 214, 222, 1)',
//             pointRadius         : false,
//             pointColor          : 'rgba(210, 214, 222, 1)',
//             pointStrokeColor    : '#c1c7d1',
//             pointHighlightFill  : '#fff',
//             pointHighlightStroke: 'rgba(220,220,220,1)',
//             data                : [65, 59, 80, 81, 56, 55, 40]
//         },
//     ]}
//     new Chart(chart, {
//         type: 'line',
//         data: areaChartData,
//         options: {
//             maintainAspectRatio: false,
//             responsive: false,
//             legend: {
//                 display: true
//             },
//             scales: {
//                 xAxes: [{
//                     gridLines: {
//                         display: false,
//                     }
//                 }],
//                 yAxes: [{
//                     gridLines: {
//                         display: false,
//                     }
//                 }]
//             }
//         }
//     });

console.log(data);

