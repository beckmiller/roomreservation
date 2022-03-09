import sqlite3
from sqlite3 import Error


def create_connection():
    """CREATE a database connection to a SQLite database"""
    conn = None
    try:
        conn = sqlite3.connect("room.db")
        return conn
    except Error as e:
        print(e)


def create_tables(conn):
    """CREATE tables"""
    sql = conn.cursor()
    sql.execute(
        """
        CREATE TABLE IF NOT EXISTS office(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            number INTEGER NOT NULL,
            person_id  INTEGER,
            start_time TEXT,
            end_time TEXT,
            date TEXT,
            FOREIGN KEY (person_id) REFERENCES person(id)
        );"""
    )
    sql.execute(
        """
        CREATE TABLE IF NOT EXISTS person(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone INT NOT NULL
        );"""
    )

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_tables(create_connection())
