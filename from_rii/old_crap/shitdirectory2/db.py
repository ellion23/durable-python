import sqlite3
con = sqlite3.connect("Database.db")
cur = con.cursor()

sql = """
CREATE TABLE IF NOT EXISTS Students (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT,
  telephone TEXT,
  birthday TEXT,
  address TEXT,
  group_id INTEGER REFERENCES "Groups"("id"),
  sports_category TEXT
);
CREATE TABLE IF NOT EXISTS Coaches (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT,
  phone TEXT,
  qualification TEXT,
  address TEXT,
  photo TEXT
);
CREATE TABLE IF NOT EXISTS Groups (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  sport_type TEXT,
  coach INTEGER REFERENCES "Coaches"("id"),
  schedule TEXT,
  month_payment REAL
);
CREATE TABLE IF NOT EXISTS Achieves (
  achieves_id INTEGER PRIMARY KEY AUTOINCREMENT,
  type TEXT,
  position INTEGER,
  student_id INTEGER REFERENCES "Students"("id")
);
"""

try:
    cur.executescript(sql)
except sqlite3.DatabaseError as err:
    print("Error:", err)
else:
    print("Tables made!")
