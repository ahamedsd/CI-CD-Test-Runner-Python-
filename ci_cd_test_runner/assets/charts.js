// Use Chart.js to display pass/fail stats
document.addEventListener('DOMContentLoaded', function () {
    const ctx = document.getElementById('results-chart').getContext('2d');

    // Sample data: dynamically populate via Python if needed
    const data = {
        labels: ['Passed', 'Failed', 'Skipped'],
        datasets: [{
            label: 'Test Results',
            data: [
                document.querySelectorAll('.passed').length,
                document.querySelectorAll('.failed').length,
                document.querySelectorAll('.skipped').length
            ],
            backgroundColor: ['#00ff00', '#ff0000', '#ffff00'],
            borderColor: ['#00ff00', '#ff0000', '#ffff00'],
            borderWidth: 1
        }]
    };

    new Chart(ctx, {
        type: 'doughnut',
        data: data,
        options: {
            responsive: true,
            plugins: {
                legend: {
                    labels: {
                        color: '#00ffff', // Cyberpunk legend color
                        font: { size: 14, weight: 'bold' }
                    }
                }
            }
        }
    });
});
