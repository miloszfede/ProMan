from flask import Flask, render_template, url_for, session, request, redirect
from dotenv import load_dotenv
from util import json_response
import mimetypes
import queries
from psycopg.sql import SQL
import bcrypt

mimetypes.add_type('application/javascript', '.js')

app = Flask(__name__)
load_dotenv()

@app.route("/")
def index():
    """
    This is a one-pager which shows all the boards and cards
    """
    return render_template('index.html')

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        password_repeat = request.form['password-repeat']
        if password == password_repeat:
            queries.add_user(login, password)
            return redirect(url_for('login_page'))
        else:
            return render_template('registration.html', error="Passwords do not match")
    return render_template('registration.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        user = queries.get_user(login, password)
        if user:
            session['username'] = user["login"]
            session['id'] = user["id"]
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error="Invalid login credentials")
    return render_template('login.html')

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route("/api/boards")
@json_response
def get_boards():
    """
    All the boards
    """
    return queries.get_boards()

@app.route("/board")
def board():
    return render_template('board.html')

@app.route("/api/boards/<int:board_id>/cards/")
@json_response
def get_cards_for_board(board_id: int):
    """
    All cards that belongs to a board
    :param board_id: id of the parent board
    """
    return queries.get_cards_for_board(board_id)


def main():
    app.run(debug=True)

    # Serving the favicon
    with app.app_context():
        app.add_url_rule('/favicon.ico', redirect_to=url_for('static', filename='favicon/favicon.ico'))


if __name__ == '__main__':
    main()
