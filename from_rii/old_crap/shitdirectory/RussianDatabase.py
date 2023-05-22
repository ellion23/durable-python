import sqlite3
from Interface import Interface
i = 0

class RussianDatabase:
    def __init__(self):
        db_name = 'SecretInfos.db'
        self.con = sqlite3.connect(db_name)
        self.cur = self.con.cursor()

    def create_table(self):
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
            self.cur.executescript(sql)
        except sqlite3.DatabaseError as err:
            print("Error:", err)
        else:
            print("Tables made!")

#           act = input('Действие (Удаление/Добавление): ')
#           if str.lower(act) == "добавление":
    def add(self):
            if str.lower(Interface.entry0) == "ученики":
                fio, birthday, address, telephone = input('ФИО;Дата рождения;Адрес;Номер телефона: ').split(';')
                sql_add = f"""
                INSERT INTO Students (fio, birthday, address, telephone)
                VALUES('{fio}', '{birthday}', '{address}', '{telephone}')
                """
            elif str.lower(Interface.entry0) == "оценки":
                id_student, subject, mark = input('Идентификатор;Предмет;Оценка: ').split(';')
                sql_add = f"""
                INSERT INTO Marks (id_student, subject, mark)
                VALUES({id_student}, '{subject}', {mark})
                """
            try:
                self.cur.execute(sql_add)
            except sqlite3.DatabaseError as err:
                print("Error:", err)
            else:
                print("Data added!")
                self.con.commit()


#        elif str.lower(act) == "удаление":
    def delete(self):
            dels = list(map(int, input().split()))
            for i in dels:
                sql_del = f"""DELETE FROM Students 
                WHERE id = {i};"""
                self.cur.execute(sql_del)
                self.con.commit()

#        sql_sel='SELECT * FROM Students;'
#        for i in cur.execute(sql_sel):
    def exit(self):
        self.cur.close()
        self.con.close()
