import sqlite3

def create_db():
    conn = sqlite3.connect("api_data.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pokemon (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        base_experience INTEGER
    );
    """)

    conn.commit()
    conn.close()
    print("Database created successfully.")

if __name__ == "__main__":
    create_db()
