import sqlite3
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
  return render_template('home.html')

@app.route("/position")
def postion():
  conn=sqlite3.connect('football.db')
  cursor=conn.cursor()
  cursor.execute('SELECT id, names FROM Position')
  positions=cursor.fetchall()
  conn.close()
  return render_template('position.html', positions=positions, title="Positions")

@app.route("/position/<int:id>")
def positionid(id):
  conn=sqlite3.connect('football.db')
  cursor=conn.cursor()
  cursor.execute('SELECT * FROM Position where id=?;', (id,))
  positionid=cursor.fetchall()
  conn.close()
  return render_template('positionid.html', positionid=positionid, title="Position")

@app.route("/player")
def player():
  conn=sqlite3.connect('football.db')
  cursor=conn.cursor()
  cursor.execute('SELECT id, name FROM Player')
  players=cursor.fetchall()
  conn.close()
  return render_template('player.html', players=players, title="Players")

@app.route("/player/<int:id>")
def playerid(id):
  conn=sqlite3.connect('football.db')
  cursor=conn.cursor()
  cursor.execute('SELECT name, info FROM Player where id=?;', (id,))
  playerid=cursor.fetchall()
  conn.close()
  return render_template('playerid.html', playerid=playerid, title="Player")

@app.route("/team")
def team():
  conn=sqlite3.connect('football.db')
  cursor=conn.cursor()
  cursor.execute('SELECT id, name FROM Team')
  teams=cursor.fetchall()
  conn.close()
  return render_template('team.html', teams=teams, title="Team")

@app.route("/team/<int:id>")
def teamid(id):
  conn=sqlite3.connect('football.db')
  cursor=conn.cursor()
  cursor.execute('SELECT name, info FROM Team where id=?;', (id,))
  teamid=cursor.fetchall()
  conn.close()
  return render_template('teamid.html', teamid=teamid, title="Team")

@app.route("/trophy")
def trophy():
  conn=sqlite3.connect('football.db')
  cursor=conn.cursor()
  cursor.execute('SELECT name FROM Trophies')
  trophy=cursor.fetchall()
  conn.close()
  return render_template('trophy.html', trophy=trophy, title="Trophy")

if __name__ == '__main__':
  app.run(port=8080, debug=True)  