$(document).ready(function() {
    $('#searchForm').on('submit', function(e) {
        e.preventDefault();
        const data = {
            make: $('#make').val(),
            model: $('#model').val(),
            top: $('#top').val(),
            cutoff: $('#cutoff').val()
        };

        $.ajax({
            url: 'http://127.0.0.1:8000/', // API Endpoint
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(data),
            success: function(response) {
                const results = JSON.parse(response.result);
                displayResults(results);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });

    $('#resetLink').on('click', function(e) {
        e.preventDefault();
        clearResults();
    });

    function displayResults(results) {
        const table = $('#resultsTable');
        table.empty(); // Clear table
        table.append('<thead><tr><th>Make</th><th>Model</th><th>Score</th></tr></thead>');
        const tbody = $('<tbody>');
        results.forEach(result => {
            const row = $('<tr>');
            row.append(`<td>${result[0][0]}</td>`);
            row.append(`<td>${result[0][1]}</td>`);
            row.append(`<td>${result[1].toFixed(3)}</td>`);
            tbody.append(row);
        });
        table.append(tbody);
    }

    function clearResults() {
        $('#resultsTable').empty();
    }
});
