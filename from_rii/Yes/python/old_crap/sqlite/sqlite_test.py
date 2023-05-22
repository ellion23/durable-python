import sqlite3
print(sqlite3.sqlite_version)
db_name = 'lib.db'
con = sqlite3.connect(db_name)

cur = con.cursor()
sql = """
CREATE TABLE IF NOT EXISTS Readers (
  id INTEGER PRIMARY KEY,
  fio TEXT,
  birthday TEXT,
  address TEXT,
  telephone TEXT
);
CREATE TABLE IF NOT EXISTS Books (
  id INTEGER PRIMARY KEY,
  title TEXT,
  author TEXT,
  year INTEGER
);
CREATE TABLE IF NOT EXISTS Lending_Books (
  id INTEGER PRIMARY KEY,
  id_reader INTEGER,
  id_book INTEGER,
  start_date TEXT DEFAULT CURRENT_DATE,
  mark BOOL
);
"""

try:
    cur.executescript(sql)
except sqlite3.DatabaseError as err:
    print("Error:", err)
else:
    print("Tables made!")
while True:
    name = input('Введите название таблицы (Читатели/Книги/Сдача книг): ')
    if str.lower(name) == "читатели" or "readers":
        fio, birthday, address, telephone = input('ФИО;Дата рождения;Адрес;Номер телефона: ').split(';')
        sql_add = f"""
        INSERT INTO Readers (fio, birthday, address, telephone)
        VALUES('{fio}', '{birthday}', '{address}', '{telephone}')
        """
    elif str.lower(name) == "книги" or "books":
        id, title, author, year = input('Идентификатор;Название;Автор;Год выпуска: ').split(';')
        sql_add = f"""
        INSERT INTO Books (id, title, author, year)
        VALUES('{id}', '{title}', '{author}', '{year}')
        """
    elif str.lower(name) == "сдача книг" or "lending books" or "lending_books":
        id, id_reader, id_book, start_date = input('Номер сдачи;Идентификатор читателя;Идентификатор книги;Дата начала: ').split(';')
        mark = bool(input("Статус сдачи(True/False): "))
        sql_add = f"""
        INSERT INTO Lending_Books (id, id_reader, id_book, start_date, mark)
        VALUES('{id}', '{id_reader}', '{id_book}', '{start_date}', '{mark}')
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