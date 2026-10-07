import sqlite3

from schemas import UserInDB

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
            "hashed_password TEXT NOT NULL)"
        )


def get_user(email: str):
    with get_connection() as connection:
        row = connection.execute(
            "SELECT name, email, hashed_password FROM users WHERE email = ?", (email,)
        ).fetchone()
    if row:
        return UserInDB(**dict(row))


def create_user(name: str, email: str, hashed_password: str):
    with get_connection() as connection:
        connection.execute(
            "INSERT INTO users (name, email, hashed_password) VALUES (?, ?, ?)",
            (name, email, hashed_password),
        )
