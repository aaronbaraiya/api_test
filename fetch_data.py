import requests
import sqlite3

def fetch_pokemon(pokemon_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    response = requests.get(url)
    data = response.json()
    return data["id"], data["name"], data["base_experience"]

def store_pokemon(pokemon):
    conn = sqlite3.connect("api_data.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT OR REPLACE INTO pokemon (id, name, base_experience) VALUES (?, ?, ?)",
        pokemon
    )

    conn.commit()
    conn.close()

def main():
    for i in range(1, 6):  # Fetch first 5 Pokémon
        pokemon = fetch_pokemon(i)
        store_pokemon(pokemon)

    print("API data fetched and stored.")

if __name__ == "__main__":
    main()
