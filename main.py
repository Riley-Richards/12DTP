import sqlite3
from flask import Flask, render_template
app = Flask(__name__)


# Simplify SQL connections for each route
def do_query(query, data = None, fetchall = False):
    conn = sqlite3.connect('football.db')
    cursor = conn.cursor()
    if data is None:
        cursor.execute(query)
    else:
        cursor.execute(query,data)
    results = cursor.fetchall() if fetchall else cursor.fetchone()
    conn.close()
    return results

#home page route
@app.route('/')
def home():
  return render_template('home.html', title="Home")

#all positions page route
@app.route("/position")
def postion():
  positions = do_query('SELECT id, names FROM Position', fetchall=True)
  return render_template('position.html', positions=positions, title="position")

#individual position page route
@app.route("/position/<int:id>")
def postionid(id):
  positionid = do_query('SELECT * FROM Position where id=?;', (id,), fetchall=False)
  return render_template('positionid.html', positionid=positionid, title="position")

#all players page route
@app.route("/players")
def players():
  players = do_query('SELECT id, name, image FROM Player', fetchall=True)
  footballteams = do_query("SELECT name FROM Team WHERE id IN (SELECT cid FROM PlayerTeams WHERE fid = id)", fetchall=True)  
  return render_template('player.html', players=players, footballteams=footballteams, title="Players")

#individual player page route
@app.route("/player/<int:id>")
def playerid(id):
  playerid = do_query('SELECT name, info, image, nation FROM Player where id=?;', (id,), fetchall=False)
  playertrophies = do_query("SELECT id, name FROM Trophies WHERE id IN (SELECT tid FROM PlayerTrophies WHERE fid = ?)", (id,), fetchall=True)
  playerteams = do_query("SELECT id, name FROM Team WHERE id IN (SELECT cid FROM PlayerTeams WHERE fid = ?)", (id,), fetchall=True)
  return render_template('playerid.html', playerid=playerid, playertrophies=playertrophies, playerteams=playerteams, title="player")

#all teams page route
@app.route("/team")
def team():
  teams = do_query('SELECT * FROM Team', fetchall=True)
  return render_template('team.html', teams=teams, title="Teams")

#individual teams page route
@app.route("/team/<int:id>")
def teamid(id):
  teamid = do_query('SELECT * FROM Team where id=?;', (id,), fetchall=False)
  teamtrophies = do_query("SELECT name FROM Trophies WHERE id IN (SELECT tid FROM TeamTrophies WHERE cid = ?)", (id,), fetchall=True)
  teamplayers = do_query("SELECT id, name FROM Player WHERE id IN (SELECT fid FROM PlayerTeams WHERE cid = ?)", (id,), fetchall=True)
  return render_template('teamid.html', teamid=teamid, teamtrophies=teamtrophies, teamplayers=teamplayers, title="team")

#all trophies page route
@app.route("/trophy")
def trophy():
  trophy = do_query('SELECT id, name FROM Trophies', fetchall=True)
  return render_template('trophy.html', trophy=trophy, title="trophy")

#individual trophy page route
@app.route("/trophy/<int:id>")
def trophyid(id):
  trophyid = do_query('SELECT * FROM Trophies where id=?;', (id,), fetchall=False)
  trophyplayers = do_query("SELECT id, name FROM Player WHERE id IN (SELECT fid FROM PlayerTrophies WHERE tid = ?)", (id,), fetchall=True)
  return render_template('trophyid.html', trophyid=trophyid, trophyplayers=trophyplayers, title="trophy")

@app.route("/squadbuilder")
def squadbuilder():
  return render_template('squad.html', title="Squadbuilder")



if __name__ == '__main__':
 app.run(port=8080, debug=True)  