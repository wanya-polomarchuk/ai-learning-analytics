import sys
import os

sys.path.append(os.path.dirname(__file__))

from database import create_table, add_entry, show_entries
from analysis import time_per_subject, time_per_type, total_learning_time, time_subject_and_type, show_all_entries
from datetime import datetime
from analysis_ai import ai_insights


create_table()

FAECHER = [
    "Mathe", 
    "Informatik", 
    "Physik", 
    "Deutsch", 
    "Englisch", 
    "Mathe Zusatz", 
    "Physik Zusatz", 
    "Geschichte", 
    "Psychologie"
]

LERN_TYPEN = [
    "Klausur",
    "Präsentation",
    "Test",
    "Hausaufgaben",
    "Stoff nachholen", 
    "Projekt"
]

def input_datum():
    while True:
        datum = input("Datum (YYYY-MM-DD): ")
        try:
            datetime.strptime(datum, "%Y-%m-%d")
            return datum
        except ValueError:
            print("Ungültiges Datum! Format: YYYY-MM-DD")


def input_fach():
    while True:
        print("Verfügbare Fächer:", ", ".join(FAECHER))
        fach = input("Fach: ")

        if fach in FAECHER:
            return fach
        else:
            print("Ungültiges Fach! Bitte aus der Liste wählen.")


def input_minuten():
    while True:
        try:
            minuten = int(input("Minuten: "))
            if minuten > 0:
                return minuten
            else:
                print("Minuten müssen größer als 0 sein.")
        except ValueError:
            print("Bitte eine Zahl eingeben.")

def input_typ():
    while True:
        print("Mögliche Lernarten:", ", ".join(LERN_TYPEN))
        typ = input("Art der Aktivität: ")

        if typ in LERN_TYPEN:
            return typ
        else:
            print("Ungültig. Bitte aus der Liste wählen.")

def input_notiz():
    return input("Notiz (optional): ")


while True:
    print("\n--- Lerntracker ---")
    print("1: Eintrag hinzufügen")
    print("2: Alle Einträge anzeigen")
    print("3: Auswertung anzeigen")
    print("4: KI-Analyse anzeigen")
    print("5: Beenden")

    choice = input("Auswahl: ")

    if choice == "1":
        datum = input_datum()
        fach = input_fach()
        minuten = input_minuten()
        typ = input_typ()
        notiz = input_notiz()

        add_entry(datum, fach, minuten, typ, notiz)

    elif choice == "2":
        show_all_entries()

    elif choice == "3":
        time_per_type()
        time_per_subject()
        time_subject_and_type()
        total_learning_time()

    elif choice == "4":
        ai_insights()

    elif choice == "5":
        break

    else:
        print("Ungültige Eingabe")