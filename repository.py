import sqlite3

DATABASE = "users.db"


def get_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def create_tables():
    with get_connection() as connection:
        connection.execute(
            "CREATE TABLE IF NOT EXISTS users ("
            "id INTEGER PRIMARY KEY AUTOINCREMENT, "
            "name TEXT NOT NULL, "
            "email TEXT NOT NULL UNIQUE, "
            "password_hash TEXT NOT NULL)"
        )


def get_user_by_email(email):
    with get_connection() as connection:
        return connection.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()


def create_user(name, email, password_hash):
    with get_connection() as connection:
        connection.execute(
            "INSERT INTO users (name, email, password_hash) VALUES (?, ?, ?)",
            (name, email, password_hash),
        )
