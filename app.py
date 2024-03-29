from flask import Flask, render_template, url_for
from flask import request, jsonify
from flask_cors import CORS
from playsound import playsound

from timer import Timer
from tasklist import Game1, Task, TaskList


app = Flask(__name__, template_folder='templates', static_folder='static')
CORS(app)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/start_pomodoro')
def start_pomodoro():
    print("pomodoro started")
    t = Timer()
    t.set_pomodoro_timer()
    t.start_timer()
    t.finish_timer()
    return {'result': 'Pomodoro started successfully'}

def custom_timer():
    # Handle custom timer logic here
    return jsonify({'result': 'Custom timer logic executed successfully'})

def button_clicked():
    pass

@app.route('/start_custom')
def start_custom():
    print("custom works")
    
if __name__ == '__main__':
    app.run(debug=True)