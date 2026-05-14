import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "lerntracker.db")

conn = sqlite3.connect(DB_PATH)


def time_per_type():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT lern_typ, SUM(minuten)
    FROM lernzeit
    GROUP BY lern_typ
    """)

    results = cursor.fetchall()

    print("\n--- Lernzeit nach Lernart ---")
    for typ, zeit in results:
        print(f"{typ}: {zeit} Minuten")

    conn.close()


def time_per_subject():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT fach, SUM(minuten)
    FROM lernzeit
    GROUP BY fach
    """)

    results = cursor.fetchall()

    print("\n--- Lernzeit nach Fach ---")
    for fach, zeit in results:
        print(f"{fach}: {zeit} Minuten")

    conn.close()


def time_subject_and_type():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT fach, lern_typ, SUM(minuten)
    FROM lernzeit
    GROUP BY fach, lern_typ
    """)

    results = cursor.fetchall()

    print("\n--- Fach und Lernart ---")
    for fach, typ, zeit in results:
        print(f"{fach} | {typ}: {zeit} Minuten")

    conn.close()


def total_learning_time():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT SUM(minuten)
    FROM lernzeit
    """)

    result = cursor.fetchone()

    total = result[0] if result[0] is not None else 0

    print("\n--- Gesamtlernzeit ---")
    print(f"{total} Minuten")

    conn.close()


def show_all_entries():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT datum, fach, minuten, lern_typ, notiz
    FROM lernzeit
    ORDER BY datum
    """)

    rows = cursor.fetchall()

    print("\n--- Alle Einträge ---")
    for datum, fach, minuten, typ, notiz in rows:
        print(f"{datum} | {fach} | {minuten} min | {typ} | Notiz: {notiz}")

    conn.close()