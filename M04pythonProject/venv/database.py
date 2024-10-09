import sqlite3

def get_db():
    conn = sqlite3.connect("books.db")
    return conn

def create_table():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        ##CREATE TABLE IF NOT EXITS books (
            #id INTEGER PRIMARY
        #book_name text NOT NULL,
        #author TEXT NOT NULL,
        #publisher TEXT NOT NULL,
    )
        
    conn.commit()
    conn.close()
    
create_table()

    