

# shared_memory/memory.py
import sqlite3
from datetime import datetime
import json

def init_db():
    conn = sqlite3.connect("memory.db")
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS memory (
            id INTEGER PRIMARY KEY,
            timestamp TEXT,
            source TEXT,
            format TEXT,
            intent TEXT,
            extracted TEXT,
            thread_id TEXT
        )
    ''')
    conn.commit()
    return conn

def log_memory(conn, source, fmt, intent, extracted, thread_id):
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO memory (timestamp, source, format, intent, extracted, thread_id)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (
        datetime.utcnow().isoformat(),
        source,
        fmt,
        intent,
        json.dumps(extracted),
        thread_id
    ))
    conn.commit()

