import sqlite3

def init_db():
    conn = sqlite3.connect('gold_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS gold_data (
            time TEXT,
            blue_gold INTEGER,
            red_gold INTEGER
        );
        DELETE FROM gold_data;
    ''')
    conn.commit()
    return conn

def insert_data(conn, game_time, blue_gold, red_gold):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO gold_data (time, blue_gold, red_gold)
        VALUES (?, ?, ?)
    ''', (game_time, blue_gold, red_gold))
    conn.commit()