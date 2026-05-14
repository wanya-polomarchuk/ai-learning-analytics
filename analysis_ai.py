from google import genai
import sqlite3

client = genai.Client()


def get_full_data():
    conn = sqlite3.connect("lerntracker.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT datum, fach, minuten, lern_typ, notiz
    FROM lernzeit
    """)

    rows = cursor.fetchall()
    conn.close()

    return rows


def ai_insights():
    data = get_full_data()

    # Daten strukturieren
    formatted_data = []
    for datum, fach, minuten, typ, notiz in data:
        formatted_data.append({
            "datum": datum,
            "fach": fach,
            "minuten": minuten,
            "typ": typ,
            "notiz": notiz
        })

    prompt = f"""
    Du bist ein Data-Analyse System. Schreibe maximal 2 Saetze pro Wert in JSON.

    Analysiere diese Lerndaten:

    {formatted_data}

    Return NUR JSON:
    {{
        "bestes_fach": "...",
        "schwaechstes_fach": "...",
        "wahrscheinlichster_typ": "...",
        "Produktivitaets-Feedback": "...",
        "Ratschlag": "..."
    }}
    """

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )

    print("\n--- KI Analyse ---")
    print(response.text)