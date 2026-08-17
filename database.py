import sqlite3
import os

# Create database folder if it doesn't exist
if not os.path.exists("database"):
    os.makedirs("database")

# Connect Database
conn = sqlite3.connect("database/grocery.db")
cursor = conn.cursor()

# Grocery Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS grocery(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    brand TEXT NOT NULL,
    selling_price REAL NOT NULL,
    mrp REAL NOT NULL,
    quantity INTEGER NOT NULL
)
""")

# Cart Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS cart(
    cart_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER,
    name TEXT,
    brand TEXT,
    selling_price REAL,
    mrp REAL,
    quantity INTEGER,
    total REAL
)
""")

conn.commit()