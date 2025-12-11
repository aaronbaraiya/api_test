# API Data Ingest Pipeline

A small Python project demonstrating a simple data ingestion pipeline:

- Fetch data from a public REST API  
- Store structured results in a SQL database  
- Query the stored data for analysis  
- Use clean, modular Python scripts for  backend workflows  

This project was done for fun while I had some spare time. 

---

## Project Overview

This pipeline retrieves Pokémon data from the public **PokéAPI**, stores it in a local SQLite database, and runs SQL queries to analyze the data.

### Key Skills Demonstrated
- Python scripting  
- Consuming REST APIs  
- SQL database creation and data insertion  
- Querying and filtering data  
- Basic ETL (Extract → Transform → Load) concepts  
- Modular code organization  
- Lightweight backend data pipeline patterns  

---

## 📂 Project Structure

api_data_ingest_pipeline/
├── fetch_data.py # Fetches data from the API and inserts into SQL
├── db_setup.py # Creates the SQLite database and table
├── query_data.py # Queries the stored API data
└── README.md # Project documentation



---

## How to Run the Project

### Install Python 

Ensure Python is installed:

python --version

---

### Create the database

python db_setup.py


This generates a `api_data.db` SQLite database with a table for Pokémon data.

---

### Fetch API data and load it into SQL

python fetch_data.py


This script calls the PokéAPI for Pokémon IDs 1–5 and inserts:

- `id`  
- `name`  
- `base_experience`  

into the SQL table.

---

### Query the data

python query_data.py


This prints all Pokémon with **base_experience > 100**, demonstrating a simple SQL filter query.

---

## Example Output

**Fetching & inserting:**

API data fetched and stored.


**Query results:**

High Experience Pokémon:
('charizard', 240)
('blastoise', 239)


---

## Database Schema

The SQLite table created:

```sql
CREATE TABLE IF NOT EXISTS pokemon (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    base_experience INTEGER
);


