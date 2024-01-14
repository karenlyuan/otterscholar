from flask import Flask, render_template, url_for

from timer import Timer
from tasklist import Game1, Task, TaskList


app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/start_pomodoro')
def start_pomodoro():
    t = Timer()
    t.set_timer("pomodero")
    t.start_time()
    t.finish_timer()
    return {'result': 'Pomodoro started successfully'}

if __name__ == '__main__':
    app.run(debug=True)