from flask import Flask, render_template, url_for
from flask import request, jsonify
from flask_cors import CORS

from timer import Timer
from tasklist import Game1, Task, TaskList


app = Flask(__name__, template_folder='templates', static_folder='static')
CORS(app)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/start_pomodoro')
def start_pomodoro():
    t = Timer()
    t.set_pomodoro_timer()
    t.start_timer()
    t.finish_timer()
    return jsonify({'timer_value': 25 * 60, 'status': 'Pomodoro started successfully'})

if __name__ == '__main__':
    app.run(debug=True)