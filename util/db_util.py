import sqlite3
import os


def get_connection():
    conn = None
    try:
        # Usa banco de teste se definido na variável de ambiente
        db_path = os.environ.get('TEST_DATABASE_PATH', 'dados.db')
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
    except sqlite3.Error as e:
        print(e)
    return conn