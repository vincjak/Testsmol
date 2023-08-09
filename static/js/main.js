document.addEventListener('DOMContentLoaded', (event) => {
    console.log('DOM fully loaded and parsed');
});

function showMessage(message) {
    let messageBox = document.getElementById('messageBox');
    messageBox.innerHTML = message;
}

function clearMessage() {
    let messageBox = document.getElementById('messageBox');
    messageBox.innerHTML = '';
}

function handleFormSubmit(event) {
    event.preventDefault();
    let form = document.getElementById('mainForm');
    let data = new FormData(form);
    fetch('/submit', {
        method: 'POST',
        body: data
    })
    .then(response => response.json())
    .then(data => {
        showMessage(data.message);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

let form = document.getElementById('mainForm');
form.addEventListener('submit', handleFormSubmit);