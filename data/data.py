import sqlite3
import os

# Database file path
current_dir = os.path.dirname(os.path.abspath(__file__))
DB_file_path = os.path.join(current_dir, "data.db")

# Function to create the table if not exists


def create_table():
    conn = sqlite3.connect(DB_file_path)
    c = conn.cursor()
    c.execute(
        '''CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY, value TEXT)''')
    conn.commit()
    conn.close()

# Function to insert data into the database


def insert_data(value):
    conn = sqlite3.connect(DB_file_path)
    c = conn.cursor()
    c.execute("INSERT INTO data (value) VALUES (?)", (value,))
    conn.commit()
    conn.close()

# Function to check if data exists in the database


def check_existing_data(value):
    conn = sqlite3.connect(DB_file_path)
    c = conn.cursor()
    c.execute("SELECT * FROM data WHERE value=?", (value,))
    result = c.fetchone()
    conn.close()
    return result is not None

# Function to display all data in the database (for debugging purposes)


def display_data():
    conn = sqlite3.connect(DB_file_path)
    c = conn.cursor()
    c.execute("SELECT * FROM data")
    result = c.fetchall()  # Fetch all rows
    conn.close()
    return result


def delete_all_data():
    try:
        conn = sqlite3.connect(DB_file_path)
        c = conn.cursor()
        c.execute("DELETE FROM data")
        conn.commit()
        conn.close()
        return "Data deleted successfully"
    except sqlite3.Error as e:
        return f"An error occurred: {e}"
