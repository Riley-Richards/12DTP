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
  cursor.execute('SELECT names FROM Position')
  position=cursor.fetchall()
  conn.close()
  return render_template('position.html', position=position, title="Positions")

@app.route("/player")
def player():
  conn=sqlite3.connect('football.db')
  cursor=conn.cursor()
  cursor.execute('SELECT name FROM Player')
  player=cursor.fetchall()
  conn.close()
  return render_template('player.html', player=player, title="Player")

@app.route("/team")
def team():
  conn=sqlite3.connect('football.db')
  cursor=conn.cursor()
  cursor.execute('SELECT name FROM Team')
  team=cursor.fetchall()
  conn.close()
  return render_template('team.html', team=team, title="Team")

@app.route("/trophy")
def trophy():
  conn=sqlite3.connect('football.db')
  cursor=conn.cursor()
  cursor.execute('SELECT name FROM Trophies')
  trophy=cursor.fetchall()
  conn.close()
  return render_template('trophy.html', trophy=trophy, title="Trophy")

@app.route("/position/<int:id>")
def positionid(id):
  conn=sqlite3.connect('football.db')
  cursor=conn.cursor()
  cursor.execute('SELECT names FROM Position where id=?;', (id,))
  positionid=cursor.fetchall()
  conn.close()
  return render_template('positionid.html', positionid=positionid, title="Position")

if __name__ == '__main__':
  app.run(port=8080, debug=True)