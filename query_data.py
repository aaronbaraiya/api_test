import sqlite3

def show_high_exp():
    conn = sqlite3.connect("api_data.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT name, base_experience 
    FROM pokemon 
    WHERE base_experience > 100;
    """)

    results = cursor.fetchall()

    print("High Experience Pokémon:")
    for r in results:
        print(r)

    conn.close()

if __name__ == "__main__":
    show_high_exp()
