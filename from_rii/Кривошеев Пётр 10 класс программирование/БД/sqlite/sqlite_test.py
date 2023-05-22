import sqlite3
print(sqlite3.sqlite_version)
db_name = '9_grade.db'
con = sqlite3.connect(db_name)

cur = con.cursor()
sql = """
CREATE TABLE IF NOT EXISTS First (
  id INTEGER PRIMARY KEY,
  monday TEXT,
  tuesday TEXT,
  wednesday TEXT,
  thursday TEXT,
  friday TEXT,
  saturday TEXT
);
CREATE TABLE IF NOT EXISTS Second (
  id INTEGER PRIMARY KEY,
  monday TEXT,
  tuesday TEXT,
  wednesday TEXT,
  thursday TEXT,
  friday TEXT,
  saturday TEXT
);
CREATE TABLE IF NOT EXISTS Third (
  id INTEGER PRIMARY KEY,
  monday TEXT,
  tuesday TEXT,
  wednesday TEXT,
  thursday TEXT,
  friday TEXT,
  saturday TEXT
);
"""

try:
    cur.executescript(sql)
except sqlite3.DatabaseError as err:
    print("Error:", err)
else:
    print("Tables made!")
while True:
    name = input('Введите название таблицы (9A/9Б/9В): ')
    if (str.lower(name) == "9а") or (str.lower(name) == "first"):
        cur.execute("SELECT * FROM First")
        res = cur.fetchall()
        monday, tuesday, wednesday, thursday, friday, saturday = input(f'понедельник, вторник, среда, четверг, пятница, суббота({len(res)+1}-й урок): ').split(', ')
        sql_add = f"""
        INSERT INTO First (monday, tuesday, wednesday, thursday, friday, saturday)
        VALUES('{monday}', '{tuesday}', '{wednesday}', '{thursday}', '{friday}', '{saturday}')
        """
    elif (str.lower(name) == "9б") or (str.lower(name) == "second"):
        cur.execute("SELECT * FROM Second")
        res = cur.fetchall()
        monday, tuesday, wednesday, thursday, friday, saturday = input(f'понедельник, вторник, среда, четверг, пятница, суббота({len(res)+1}-й урок): ').split(', ')
        sql_add = f"""                                                                               
        INSERT INTO Second (fio, birthday, address, telephone)                                      
        VALUES('{monday}', '{tuesday}', '{wednesday}', '{thursday}', '{friday}', '{saturday}')       
        """
    elif (str.lower(name) == "9в") or (str.lower(name) == "third"):
        cur.execute("SELECT * FROM Third")
        res = cur.fetchall()
        monday, tuesday, wednesday, thursday, friday, saturday = input(f'понедельник, вторник, среда, четверг, пятница, суббота({len(res)+1}-й урок): ').split(', ')
        sql_add = f"""                                                                               
        INSERT INTO Third (fio, birthday, address, telephone)                                      
        VALUES('{monday}', '{tuesday}', '{wednesday}', '{thursday}', '{friday}', '{saturday}')       
        """

    else:
        print('Таблицы не существует.')
        break
    try:
        cur.execute(sql_add)
    except sqlite3.DatabaseError as err:
        print("Error:", err)
    else:
        print("Data added!")
        con.commit()
    break

cur.close()
con.close()
