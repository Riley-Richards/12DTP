import sqlite3
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
  return render_template('home.html')

@app.route("/position")
def postions():
  return render_template('position.html')
  
if __name__ == '__main__':
  app.run(port=8080)