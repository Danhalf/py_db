# db_utils.py
# -*- coding: utf-8 -*-

import sqlite3

def connect_db(db_path):
    conn = sqlite3.connect(db_path)
    return conn

def execute_schema(conn):
    cursor = conn.cursor()
    with open('db/schema.sql', 'r') as schema_file:
        schema = schema_file.read()
    cursor.executescript(schema)
    conn.commit()

def get_records(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tech")
    return cursor.fetchall()

def add_record(conn, name, number, owner, status, notes):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tech (name, number, owner, status, notes) VALUES (?, ?, ?, ?, ?)", 
                   (name, number, owner, status, notes))
    conn.commit()