from flask import Flask, render_template
from nba_api.live.nba.endpoints import scoreboard
from nba_api.stats.endpoints import teamgamelog
import json

teams = {'CLE': 1610612739, 'OKC': 1610612760, 'BOS': 1610612738, 'DEN': 1610612743, 'NYK': 1610612752, 'MEM': 1610612763, 'HOU': 1610612745, 'IND': 1610612754, 'LAL': 1610612747, 'MIL': 1610612749, 'LAC': 1610612746, 'DET': 1610612765, 'MIN': 1610612750, 'ORL': 1610612753, 'DAL': 1610612742, 'MIA': 1610612748, 'ATL': 1610612737, 'SAC': 1610612758, 'CHI': 1610612741, 'GSW': 1610612744, 'PHI': 1610612755, 'PHX': 1610612756, 'BKN': 1610612751, 'SAS': 1610612759, 'POR': 1610612757, 'TOR': 1610612761, 'UTA': 1610612762, 'CHA': 1610612766, 'NOP': 1610612740, 'WAS': 1610612764}

app = Flask(__name__)

@app.route('/')
def home():
    games = scoreboard.ScoreBoard().get_dict()
    return render_template('scoreboard.html', games = games["scoreboard"]["games"])

@app.route('/season/<teamName>')
def season(teamName):

    season = json.loads(teamgamelog.TeamGameLog(team_id=teams[teamName], season_type_all_star="Regular Season", season="2024-25").get_json())["resultSets"][0]["rowSet"]
    return render_template('season.html', season=season)


app.run(host="0.0.0.0")