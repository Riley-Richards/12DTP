import sqlite3
from flask import Flask, render_template, request, redirect

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
  return render_template('position.html', title="position")

#individual position page route
@app.route("/position/<int:id>")
def postionid(id):
  positionid = do_query('SELECT * FROM Position where id=?;', (id,), fetchall=False)
  playerp = do_query('SELECT * FROM Player where pid=?;', (id,), fetchall=True)
  return render_template('positionid.html', positionid=positionid, playerp=playerp, title="position")

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
  teamtrophies = do_query("SELECT id, name, image FROM Trophies WHERE id IN (SELECT tid FROM TeamTrophies WHERE cid = ?)", (id,), fetchall=True)
  teamplayers = do_query("SELECT id, name, image FROM Player WHERE id IN (SELECT fid FROM PlayerTeams WHERE cid = ?)", (id,), fetchall=True)
  return render_template('teamid.html', teamid=teamid, teamtrophies=teamtrophies, teamplayers=teamplayers, title="team")

#all trophies page route
@app.route("/trophy")
def trophy():
  trophy = do_query('SELECT id, name, image FROM Trophies', fetchall=True)
  return render_template('trophy.html', trophy=trophy, title="trophy")

#individual trophy page route
@app.route("/trophy/<int:id>")
def trophyid(id):
  trophyid = do_query('SELECT * FROM Trophies where id=?;', (id,), fetchall=False)
  trophyplayers = do_query("SELECT id, name FROM Player WHERE id IN (SELECT fid FROM PlayerTrophies WHERE tid = ?)", (id,), fetchall=True)
  return render_template('trophyid.html', trophyid=trophyid, trophyplayers=trophyplayers, title="trophy")

#squad builder page route
@app.route("/squadbuilder")
def squadbuilder():
  return render_template('squad.html', title="Squadbuilder")

#404 ERROR page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'), 404

@app.route ("/search", methods=["POST", "GET"])
def search():
    #search bar.
    if request.method == "POST":
        print (request.form.get("filter"))
        results = do_query("SELECT * FROM Player WHERE Player.name LIKE '%' || ? || '%' ORDER BY Player.name;", (request.form.get("filter"),), fetchall = True)
        if results == None:
            return redirect ("/error")
        else:
            return render_template("searchresults.html", results = results, title = "Search Results")




if __name__ == '__main__':
 app.run(port=8080, debug=True)  