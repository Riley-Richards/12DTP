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
  cursor.execute('SELECT id FROM Position', (id,))
  position=cursor.fetchone()
  conn.close()
  return render_template('position.html')
  
if __name__ == '__main__':
  app.run(port=8080, debug=True)