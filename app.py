from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session

questions = {
    "What is the keyword to define a function in Python?": "def",
    "Which data type is used to store True or False values?": "boolean",
    "What is the correct file extension for Python files?": ".py",
    "Which symbol is used to comment in Python?": "#",
    "What function is used to get input from the user?": "input",
    "How do you start a for loop in Python?": "for",
    "What is the output of 2 ** 3 in Python?": "8",
    "What keyword is used to import a module in Python?": "import",
    "What does the len() function return?": "length",
    "What is the result of 10 // 3 in Python?": "3"
}

@app.route('/')
def index():
    # Select 5 random questions
    selected = random.sample(list(questions.items()), 5)
    session['quiz'] = selected  # store in session
    return render_template('quiz.html', questions=selected)

@app.route('/submit', methods=['POST'])
def submit():
    quiz = session.get('quiz')
    score = 0

    for i, (q, correct) in enumerate(quiz):
        user_answer = request.form.get(f'q{i}', '').strip().lower()
        if user_answer == correct.lower():
            score += 1

    return render_template('result.html', score=score, total=len(quiz))

if __name__ == '__main__':
    app.run(debug=True)

