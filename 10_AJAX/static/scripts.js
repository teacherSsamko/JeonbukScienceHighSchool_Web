document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('getQuoteBtn').addEventListener('click', function () {
        fetch('/random_quote')
            .then(response => response.json())
            .then(data => {
                document.getElementById('quoteDisplay').innerText = data;
            })
            .catch(error => console.error('Error:', error));
    });
});