import data_manager
from psycopg.sql import SQL
import bcrypt

def get_card_status(status_id):
    """
    Find the first status matching the given id
    :param status_id:
    :return: str
    """
    status = data_manager.execute_select(
        """
        SELECT * FROM statuses s
        WHERE s.id = %(status_id)s
        ;
        """
        , {"status_id": status_id})

    return status


def get_boards():
    """
    Gather all boards
    :return:
    """
    # remove this code once you implement the database
    return [{"title": "board1", "id": 1}, {"title": "board2", "id": 2}]

    return data_manager.execute_select(
        """
        SELECT * FROM boards
        ;
        """
    )


def get_cards_for_board(board_id):
    # remove this code once you implement the database
    return [{"title": "title1", "id": 1}, {"title": "board2", "id": 2}]

    matching_cards = data_manager.execute_select(
        """
        SELECT * FROM cards
        WHERE cards.board_id = %(board_id)s
        ;
        """
        , {"board_id": board_id})

    return matching_cards


def get_board_title():
    return [{"title"}]
    return data_manager.execute_select(
        """
        SELECT title FROM boards
        ;
        """
    )

def add_user(cursor, login, password):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    cursor.execute(
        SQL("INSERT INTO users (login, password) VALUES (%(login)s, %(password)s) RETURNING id"),
        {'login': login, 'password': hashed_password.decode('utf-8')}
    )
    return cursor.fetchone()['id']


def get_user(cursor, login, password):
    cursor.execute(
        SQL("SELECT * FROM users WHERE login = %(login)s"),
        {'login': login}
    )
    user = cursor.fetchone()
    if user and bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
        return user
    return None
