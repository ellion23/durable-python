import sqlite3


i = 0
print(sqlite3.sqlite_version)
db_name = 'marks_lib.db'
con = sqlite3.connect(db_name)

cur = con.cursor()
sql = """
CREATE TABLE IF NOT EXISTS Students (
  id INTEGER PRIMARY KEY,
  fio TEXT,
  birthday TEXT,
  address TEXT,
  telephone TEXT
);
CREATE TABLE IF NOT EXISTS Marks (
  id_student INTEGER,
  subject TEXT,
  mark INTEGER
);
"""

try:
    cur.executescript(sql)
except sqlite3.DatabaseError as err:
    print("Error:", err)
else:
    print("Tables made!")

act = input('Действие (Удаление/Добавление): ')
if str.lower(act) == "добавление":
    name = input('Введите название таблицы (Ученики/Оценки): ')
    if str.lower(name) == "ученики":
        fio, birthday, address, telephone = input('ФИО;Дата рождения;Адрес;Номер телефона: ').split(';')
        sql_add = f"""
        INSERT INTO Students (fio, birthday, address, telephone)
        VALUES('{fio}', '{birthday}', '{address}', '{telephone}')
        """
    elif str.lower(name) == "оценки":
        id_student, subject, mark = input('Идентификатор;Предмет;Оценка: ').split(';')
        sql_add = f"""
        INSERT INTO Marks (id_student, subject, mark)
        VALUES({id_student}, '{subject}', {mark})
        """
    try:
        cur.execute(sql_add)
    except sqlite3.DatabaseError as err:
        print("Error:", err)
    else:
        print("Data added!")
        con.commit()


elif str.lower(act) == "удаление":
    dels = list(map(int, input().split()))
    for i in dels:
        sql_del = f"""DELETE FROM Students 
        WHERE id = {i};"""
        cur.execute(sql_del)
        con.commit()

sql_sel = 'SELECT * FROM Students;'
#for i in cur.execute(sql_sel):
cur.close()
con.close()
