import sqlite3
from flask import Flask, render_template, request, redirect, abort

app = Flask(__name__)


# Simplify SQL connections for each route
def do_query(query, data=None, fetchall=False):
    conn = sqlite3.connect('football.db')
    cursor = conn.cursor()
    if data is None:
        cursor.execute(query)
    else:
        cursor.execute(query, data)
    results = cursor.fetchall() if fetchall else cursor.fetchone()
    conn.close()
    return results


# home page route
@app.route('/')
def home():
    return render_template('home.html', title="Home")


# all positions page route
@app.route("/position")
def postion():
    return render_template('position.html', title="position")


# individual position page route
@app.route("/position/<string:id>")
def postionid(id):
    position_id = do_query('SELECT * FROM Position where id=?;', (id, ),
                           fetchall=False)
    player_position = do_query(
        """SELECT id, name, image FROM
        Player where pid=?;""",
        (id, ),
        fetchall=True)
    if position_id is None:
        abort(404)
    return render_template('positionid.html',
                           position_id=position_id,
                           player_position=player_position,
                           title="position")


# all players page route
@app.route("/players")
def players():
    players = do_query('SELECT id, name, image FROM Player', fetchall=True)
    return render_template('player.html',
                           players=players,
                           title="Players")


# individual player page route
@app.route("/player/<string:id>")
def playerid(id):
    player_id = do_query(
        'SELECT name, info, image, nation FROM Player where id=?;', (id, ),
        fetchall=False)
    # pulls the data from the trophies table where the corressponding
    # player's id matches the trophy id in the PlayerTrophies table
    player_trophies = do_query(
        """SELECT id, name, image FROM Trophies
        WHERE id IN (SELECT tid FROM PlayerTrophies
        WHERE fid = ?)""",
        (id, ),
        fetchall=True)
    # pulls the data from the team table where the corresponding
    # player's id matches the team id in the PlayerTeams table
    player_teams = do_query(
        """SELECT id, name, image FROM Team
        WHERE id IN (SELECT cid FROM PlayerTeams
        WHERE fid = ?)""",
        (id, ),
        fetchall=True)
    if player_id is None:
        abort(404)
    return render_template('playerid.html',
                           player_id=player_id,
                           player_trophies=player_trophies,
                           player_teams=player_teams,
                           title="player")


# all teams page route
@app.route("/team")
def team():
    teams = do_query('SELECT id, name, image FROM Team', fetchall=True)
    return render_template('team.html', teams=teams, title="Teams")


# individual teams page route
@app.route("/team/<string:id>")
def teamid(id):
    team_id = do_query(
        """SELECT id, name, image, info FROM
        Team where id=?;""",
        (id, ),
        fetchall=False)
    # pulls the data from the trophies table where the corresponding
    # team's id matches the trophy id in the TeamTrophies table
    team_trophies = do_query(
        """SELECT id, name, image FROM Trophies WHERE
        id IN (SELECT tid FROM TeamTrophies WHERE cid = ?)""",
        (id, ),
        fetchall=True)
    # pulls the data from the players table where the corresponding
    # team's id matches the player id in the PlayerTeam table
    team_players = do_query(
        """SELECT id, name, image FROM Player WHERE id IN
        (SELECT fid FROM PlayerTeams WHERE cid = ?)""",
        (id, ),
        fetchall=True)
    if team_id is None:
        abort(404)
    return render_template('teamid.html',
                           team_id=team_id,
                           team_trophies=team_trophies,
                           team_players=team_players,
                           title="team")


# all trophies page route
@app.route("/trophy")
def trophy():
    trophy = do_query('SELECT id, name, image FROM Trophies', fetchall=True)
    return render_template('trophy.html', trophy=trophy, title="trophy")


# individual trophy page route
@app.route("/trophy/<string:id>")
def trophyid(id):
    trophy_id = do_query('SELECT * FROM Trophies where id=?;', (id, ),
                         fetchall=False)
    # pulls the data from the players table where the corresponding
    # trophy's id matches the player id in the PlayerTrophies table
    trophy_players = do_query(
        """SELECT id, name, image FROM Player WHERE id IN
        (SELECT fid FROM PlayerTrophies WHERE tid = ?)""",
        (id, ),
        fetchall=True)
    # pulls the data from the teams table where the corresponding
    # trophy's id matches the team id in the TeamTrophies table
    trophy_teams = do_query(
        """SELECT id, name, image FROM Team
        WHERE id IN (SELECT cid
        FROM TeamTrophies WHERE tid = ?)""",
        (id, ),
        fetchall=True)
    if trophy_id is None:
        abort(404)
    return render_template('trophyid.html',
                           trophy_id=trophy_id,
                           trophy_players=trophy_players,
                           trophy_teams=trophy_teams,
                           title="trophy")


# squadbuilder route
@app.route("/squadbuilder")
def squadbuilder():
    return render_template('squad.html')


# squad builder page route
@app.route("/squad", methods=["POST"])
def squad():
    connection = sqlite3.connect('football.db')
    cursor = connection.cursor()
    # gives the user a box to type their input for each player they want
    name = request.form["name"]
    gk = request.form["gk"]
    rb = request.form["rb"]
    center_back = request.form["center_back"]
    lcb = request.form["lcb"]
    lb = request.form["lb"]
    cdm = request.form["cdm"]
    cm = request.form["cm"]
    cam = request.form["cam"]
    lw = request.form["lw"]
    rw = request.form["rw"]
    st = request.form["st"]
    # sends the user inputs into their corresponding column on
    # the squadbuilder page
    sql = """INSERT INTO squadbuilder
    (name, gk, lb, rcb, lcb, rb, cdm, cm, cam, lw, rw, st)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
    cursor.execute(
        sql, (name, gk, lb, center_back, lcb, rb, cdm, cm, cam, lw, rw, st))
    connection.commit()
    connection.close()
    submit = True
    return render_template('squad.html')


# page to display all user created teams
@app.route("/allsquads")
def allsquads():
    allsquads = do_query("SELECT id, name FROM squadbuilder",
                         data=None,
                         fetchall=True)
    return render_template('allsquads.html', allsquads=allsquads)


# page to display individual user created team
@app.route("/squad/<string:id>")
def user_squad(id):
    user_squad = do_query('SELECT * FROM squadbuilder where id=?;', (id, ),
                          fetchall=False)
    if user_squad is None:
        abort(404)
    return render_template('usersquad.html', user_squad=user_squad)


# 404 ERROR page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'), 404


# contact route
@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')


# page for user to input contact details and message
submit = None


@app.route("/message", methods=["POST"])
def message():
    connection = sqlite3.connect('football.db')
    cursor = connection.cursor()
    # gives the user input boxes for them to input
    # their name, email and message
    user_first_name = request.form["user_first_name"]
    user_last_name = request.form["user_last_name"]
    user_email = request.form["user_email"]
    user_message = request.form["user_message"]
    # inserts the user inputs into the contact table in my database
    sql = """INSERT INTO contact
    (user_first_name, user_last_name, user_email, user_message)
    VALUES (?, ?, ?, ?)"""
    cursor.execute(sql,
                   (user_first_name, user_last_name, user_email, user_message))
    connection.commit()
    connection.close()
    submit = True
    return render_template('contact.html', submit=submit)


# search bar for searching players
@app.route('/search', methods=["POST", "GET"])
def search():
    if request.method == "POST":
        # this filter sends the user to the player page
        # with a matching section of string
        print(request.form.get("filter"))
        search = do_query(
            f'''SELECT * FROM Player WHERE Player.name
            LIKE "%" || ? || "%" ORDER BY Player.name;''',
            (request.form.get("filter"), ),
            fetchall=True)
            # this query selects everything in the player table
        if len(search) == 0:
            return redirect('/error')
        elif request.form.get("filter") == '':
            return redirect('/error')
            # these if statements send the user to the error page
            # if there search has no length or blank
        else:
            return redirect(f'/player/{(search[0])[0]}')
            # this sends the user to the individuals
            # players page


# about page for image and data sources
@app.route('/about')
def about():
    return render_template('about.html')

# runs port on local site
if __name__ == '__main__':
    app.run(port=8080, debug=True)
