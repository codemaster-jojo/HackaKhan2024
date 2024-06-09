document.addEventListener('DOMContentLoaded', function () {
    const completeButton = document.getElementById('complete-btn');
    completeButton.addEventListener('click', function () {
        fetch('/complete_lesson', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                lesson_id: {{ lesson.id }}
            })
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
        })
        .catch(error => console.error('Error:', error));
    });
});