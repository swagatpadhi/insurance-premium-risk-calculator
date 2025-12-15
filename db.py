# import sqlite3

# #Database setup

# db_path = "database/insurance.db"

# # Create Database function
# def get_db_connection():
#     conn = sqlite3.connect(db_path)
#     return conn

# #Create table function
# def create_table():
#     conn = get_db_connection()
#     cursor = conn.cursor()

#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS insurance_records (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         age INTEGER,
#         vehicle_type TEXT,
#         engine_type TEXT,
#         vehicle_value INTEGER,
#         location TEXT,
#         accidents INTEGER,
#         premium INTEGER,
#         risk TEXT
#     )
#     """)

#     conn.commit()
#     conn.close()


# # insert value
# def insert_record(age, vehicle_type, engine_type, vehicle_value, location, accidents, premium, risk):
#     conn = get_db_connection()
#     cursor = conn.cursor()
    
#     cursor.execute("""
#         INSERT INTO insurance_records
#         (age, vehicle_type, engine_type, vehicle_value, location, accidents,
#          risk_score, risk_level, premium, created_at)
#         VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
#     """, (
#         age, 
#         vehicle_type, 
#         engine_type,
#         vehicle_value, 
#         location,
#         accidents,     
#         premium,
#         risk
#     ))
    
#     conn.commit()
#     conn.close()

import sqlite3
import os

DB_PATH = "database/insurance.db"

def get_db_connection():
    os.makedirs("database", exist_ok=True)
    return sqlite3.connect(DB_PATH)

def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS insurance_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            age INTEGER,
            vehicle_type TEXT,
            engine_type TEXT,
            vehicle_value INTEGER,
            location TEXT,
            accidents INTEGER,
            premium INTEGER,
            risk INTEGER,
            risk_level TEXT
        )
    """)

    conn.commit()
    conn.close()

def insert_record(
    age,
    vehicle_type,
    engine_type,
    vehicle_value,
    location,
    accidents,
    premium,
    risk,
    risk_level
):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO insurance_records
        (age, vehicle_type, engine_type, vehicle_value, location, accidents, premium, risk, risk_level)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        age,
        vehicle_type,
        engine_type,
        vehicle_value,
        location,
        accidents,
        premium,
        risk,
        risk_level
    ))

    conn.commit()
    conn.close()
