import sqlite3

def get_connection():
    conn = sqlite3.connect("students.db")
    return conn

def initialize_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id TEXT PRIMARY KEY,
            name TEXT,
            english INTEGER,
            c_language INTEGER,
            python INTEGER,
            total INTEGER,
            average REAL,
            grade TEXT,
            rank INTEGER
        )
    ''')
    conn.commit()
    conn.close()