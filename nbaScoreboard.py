from flask import Flask, render_template
from nba_api.live.nba.endpoints import scoreboard



app = Flask(__name__)

@app.route('/')
def home():
    games = scoreboard.ScoreBoard().get_dict()
    return render_template('scoreboard.html', games = games["scoreboard"]["games"])

app.run(host="0.0.0.0")