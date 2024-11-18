from flask import Flask, render_template
from nba_api.live.nba.endpoints import scoreboard

games = scoreboard.ScoreBoard().get_json()

app = Flask(__name__)

@app.route('/')
def scoreboard():
    return render_template('scoreboard.html', games = games)