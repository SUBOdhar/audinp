import sqlite3


def create_table():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS words
                 (id INTEGER PRIMARY KEY, word TEXT)''')
    conn.commit()
    conn.close()


def add_word(word):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("INSERT INTO words (word) VALUES (?)", (word,))
    conn.commit()
    conn.close()


def main():
    create_table()
    print("Welcome to the word entry system!")
    while True:
        word = input("Enter a word (or 'quit' to exit): ")
        if word.lower() == 'quit':
            break
        add_word(word)
        print("Word added successfully!\n")


if __name__ == "__main__":
    main()
