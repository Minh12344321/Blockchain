function mineBlock() {
    fetch('http://127.0.0.1:5000/mine')
    .then(response => response.json())
    .then(data => document.getElementById('output').innerText = JSON.stringify(data, null, 2))
    .catch(error => console.error('Error:', error));
}

function viewChain() {
    fetch('http://127.0.0.1:5000/chain')
    .then(response => response.json())
    .then(data => document.getElementById('output').innerText = JSON.stringify(data, null, 2))
    .catch(error => console.error('Error:', error));
}
