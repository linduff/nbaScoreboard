from flask import Flask, render_template
from nba_api.live.nba.endpoints import scoreboard
from nba_api.stats.endpoints import teamgamelog, scoreboardv2
import json

teams = {'CLE': 1610612739, 'OKC': 1610612760, 'BOS': 1610612738, 'DEN': 1610612743, 'NYK': 1610612752, 'MEM': 1610612763, 'HOU': 1610612745, 'IND': 1610612754, 'LAL': 1610612747, 'MIL': 1610612749, 'LAC': 1610612746, 'DET': 1610612765, 'MIN': 1610612750, 'ORL': 1610612753, 'DAL': 1610612742, 'MIA': 1610612748, 'ATL': 1610612737, 'SAC': 1610612758, 'CHI': 1610612741, 'GSW': 1610612744, 'PHI': 1610612755, 'PHX': 1610612756, 'BKN': 1610612751, 'SAS': 1610612759, 'POR': 1610612757, 'TOR': 1610612761, 'UTA': 1610612762, 'CHA': 1610612766, 'NOP': 1610612740, 'WAS': 1610612764}

def formatScoreboardData():
    games = []
    scoreboardData = scoreboardv2.ScoreboardV2().get_dict()
    gameHeaders = scoreboardData["resultSets"][0]["rowSet"]
    lineScores = scoreboardData["resultSets"][1]["rowSet"]
    for game in gameHeaders:
        
        homeLS = ([item for item in lineScores if item[3] == game[6]])[0]
        awayLS = ([item for item in lineScores if item[3] == game[7]])[0]

        home_wins, home_losses = homeLS[7].split("-")
        away_wins, away_losses = awayLS[7].split("-")

        games.append({
            "game_id": game[2],
            "game_status_id": game[3],
            "game_status_text": game[4],
            "home_id": game[6],
            "home_abbreviation": homeLS[4],
            "home_location": homeLS[5],
            "home_name": homeLS[6],
            "home_wins": home_wins,
            "home_losses": home_losses,
            "home_points": homeLS[22],
            "home_q1": "-" if homeLS[8] == None else homeLS[8],
            "home_q2": "-" if homeLS[9] == None else homeLS[9],
            "home_q3": "-" if homeLS[10] == None else homeLS[10],
            "home_q4": "-" if homeLS[11] == None else homeLS[11],
            "home_ot1": "-" if homeLS[12] == None else homeLS[12],
            "home_ot2": "-" if homeLS[13] == None else homeLS[13],
            "home_ot3": "-" if homeLS[14] == None else homeLS[14],
            "home_ot4": "-" if homeLS[15] == None else homeLS[15],
            "home_ot5": "-" if homeLS[16] == None else homeLS[16],
            "home_ot6": "-" if homeLS[17] == None else homeLS[17],
            "away_id": game[7],
            "away_abbreviation": awayLS[4],
            "away_location": awayLS[5],
            "away_name": awayLS[6],
            "away_wins": away_wins,
            "away_losses": away_losses,
            "away_points": awayLS[22],
            "away_q1": "-" if awayLS[8] == None else awayLS[8],
            "away_q2": "-" if awayLS[9] == None else awayLS[9],
            "away_q3": "-" if awayLS[10] == None else awayLS[10],
            "away_q4": "-" if awayLS[11] == None else awayLS[11],
            "away_ot1": "-" if awayLS[12] == None else awayLS[12],
            "away_ot2": "-" if awayLS[13] == None else awayLS[13],
            "away_ot3": "-" if awayLS[14] == None else awayLS[14],
            "away_ot4": "-" if awayLS[15] == None else awayLS[15],
            "away_ot5": "-" if awayLS[16] == None else awayLS[16],
            "away_ot6": "-" if awayLS[17] == None else awayLS[17],
        })
    return games

app = Flask(__name__)

# scoreboardData = scoreboardv2.ScoreboardV2().get_dict()
# gameHeaders = scoreboardData["resultSets"][0]["rowSet"]
# lineScores = scoreboardData["resultSets"][1]["rowSet"]
# print(gameHeaders)
# print(lineScores)
# homeLS = [item for item in lineScores if item[3] == gameHeaders[0][6]]
# print(homeLS)
# home_wins, home_losses = homeLS[0][7].split("-")
# print(home_wins)
# print(home_losses)



@app.route('/')
def home():
    scoreboardGames = formatScoreboardData()
    
    return render_template('scoreboard.html', games = scoreboardGames)

@app.route('/season/<teamName>')
def season(teamName):

    season = json.loads(teamgamelog.TeamGameLog(team_id=teams[teamName], season_type_all_star="Regular Season", season="2024-25").get_json())["resultSets"][0]["rowSet"]
    return render_template('season.html', season=season)


app.run(host="0.0.0.0")


