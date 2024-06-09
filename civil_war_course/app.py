from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

lessons = [
    {
        'id': 1,
        'title': 'What Led to the Civil War?',
        'content': 'This lesson covers the causes of the Civil War.',
        'points': 100
    },
]

@app.route('/')
def index():
    return render_template('index.html', lessons=lessons)

@app.route('/lesson1')
def lesson1():
    return render_template('lesson1.html', lesson=lessons[0])


@app.route('/complete_lesson', methods=['POST'])
def complete_lesson():
    data = request.get_json()
    lesson_id = data.get('lesson_id')
    # Logic to mark lesson as completed and update user points
    return jsonify({'success': True})

if __name__ == "__main__":
    app.run(debug=True, port=5002)