import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "lerntracker.db")

conn = sqlite3.connect(DB_PATH)


def create_table():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS lernsession (
        id INTEGER PRIMARY KEY,
        datum TEXT,
        minuten INTEGER,
        lern_typ TEXT,
        notiz TEXT,
        fach TEXT
    )
    """)

    conn.commit()
    conn.close()


def add_entry(datum, fach, minuten, lern_typ, notiz):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO lernzeit (datum, fach, minuten, lern_typ, notiz) VALUES (?, ?, ?, ?, ?)",
        (datum, fach, minuten, lern_typ, notiz)
    )

    conn.commit()
    conn.close()


def show_entries():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM lernzeit")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()