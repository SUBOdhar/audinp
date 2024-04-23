import sqlite3


def fetch_table_data(database_path, table_name):
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        # Fetch all data from the specified table
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()

        # Close the database connection
        conn.close()

        return rows

    except sqlite3.Error as e:
        print("SQLite error:", e)
        return []


# Specify the path to your SQLite database file
database_path = 'nep_dict.sqlite3'

# Fetch data from the 'word' table
word_data = fetch_table_data(database_path, 'word')

# Print 'word' table data with tabs
print("Word Table:")
for row in word_data:
    print('\t'.join(map(str, row)))

# Fetch data from the 'definition' table
definition_data = fetch_table_data(database_path, 'definition')

# Print 'definition' table data with tabs
print("\nDefinition Table:")
for row in definition_data:
    print('\t'.join(map(str, row)))

# Fetch data from the 'example' table
example_data = fetch_table_data(database_path, 'example')

# Print 'example' table data with tabs
print("\nExample Table:")
for row in example_data:
    print('\t'.join(map(str, row)))
