from sleeper_wrapper import League
import requests
import json
import datetime

league_id = '814091731229319168'
notif = 0

# Get json from sleeper for player ID
url = requests.get('https://api.sleeper.app/v1/players/nba')
text = url.text
data = json.loads(text)

# Get my roster
league = League(league_id)
r = league.get_rosters()
my_r = r[7]
my_starters = r[7]['starters']

# Get team from ID players
team = []
for i in my_starters:
    for j in data:
        if i == j:
            new_team = data[j]['team']
            if new_team not in team:
                team.append(new_team)

# Translate team from sleeper for nba name
team_nba = {
    "TOR": "Raptors",
    "SAC": "Kings",
    "MEM": "Grizzlies",
    "NOP": "Pelicans",
    "WAS": "Wizards",
    "ATL": "Hawks",
    "PHX": "Suns",
    "CLE": "Cavaliers",
    "IND": "Pacers",
    "SAS": "Spurs",
    "HOU": "Rockets",
    "POR": "Trail Blazers",
    "UTA": "Jazz",
    "LAL": "Lakers",
    "OKC": "Thunder",
    "DEN": "Nuggets",
    "NYK": "Knicks",
    "CHA": "Hornets",
    "LAC": "Clippers",
    "PHI": "76ers",
    "MIA": "Heat",
    "MIN": "Timberwolves",
    "BOS": "Celtics",
    "DAL": "Mavericks",
    "DET": "Pistons",
    "GSW": "Warriors",
    "CHI": "Bulls",
    "BKN": "Nets",
    "ORL": "Magic",
    "MIL": "Bucks",
}

teamn = []
for i in team:
    teamn.append(team_nba[i])

# Get shedule from day before
pre_url = 'https://www.nba.com/games?date='
match_day = datetime.date.today()-datetime.timedelta(1)
match_day = match_day.strftime('%Y-%m-%d')
url_match_day = pre_url + str(match_day)

# Check if team played
url_shedule = requests.get(url_match_day)
text = url.text
for i in teamn:
    if i in text:
        notif = 1
    break

# Send notification to my phone
if notif == 1:
    requests.post("https://maker.ifttt.com/trigger/{event}/json/with/key/{secret_key}")
