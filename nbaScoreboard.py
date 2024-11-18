from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def scoreboard():
    return render_template('scoreboard.html')