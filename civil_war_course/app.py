from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

lessons = [
    {
        'id': 1,
        'title': 'Causes of the Civil War',
        'content': 'This lesson covers the causes of the Civil War.',
        'points': 100
    },
    {
        'id': 2,
        'title': 'Key Battles',
        'content': 'This lesson covers key battles of the Civil War.',
        'points': 150
    },
    {
        'id': 3,
        'title': 'The Aftermath of the Civil War',
        'content': 'This lesson covers the period following the end of the Civil War.',
        'points': 150
    },
]

@app.route('/')
def index():
    return render_template('index.html', lessons=lessons)

@app.route('/lesson1')
def lesson1():
    return render_template('lesson1.html', lesson=lessons[0])

@app.route('/lesson2')
def lesson2():
    return render_template('lesson2.html', lesson=lessons[1])

@app.route('/lesson3')
def lesson3():
    return render_template('lesson3.html', lesson=lessons[2])

@app.route('/complete_lesson', methods=['POST'])
def complete_lesson():
    data = request.get_json()
    lesson_id = data.get('lesson_id')
    # Logic to mark lesson as completed and update user points
    return jsonify({'success': True})

if __name__ == "__main__":
    app.run(debug=True, port=5002)
