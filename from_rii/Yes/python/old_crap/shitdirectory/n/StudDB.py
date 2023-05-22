import sqlite3

class Student:
    """
    Класс для описания данных о студенте.
    """
    def __init__(self, FIO, Class, Telephone, Adress):
        self.FIO = FIO
        self.Class = Class
        self.Telephone = Telephone
        self.Adress = Adress

class StudentsDB:
    """
    Класс для работы с базой данных о студентах.
    """
    def __init__(self):
        self.db_name = 'school.db'
        self.con = sqlite3.connect(self.db_name)
        self.cur = self.con.cursor()  # Создать объект-курсор

    def create_table(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Students(
            id INTEGER PRIMARY KEY,
            fio TEXT,
            class INTEGER,
            telephone TEXT,
            address TEXT
        );
        CREATE TABLE IF NOT EXISTS Marks (
            subject TEXT,
            mark INTEGER,
            id_student INTEGER 
        );
        """
        try:
            self.cur.executescript(sql)  # Выполнить запросы.
        except sqlite3.DatabaseError as err:
            print("Error:", err)
        else:
            print("Таблицы созданы")

    def add_student(self, student):
        print(student)
        sql = f"""
            INSERT INTO Students(fio, class, telephone, address)
            VALUES ('{student.FIO}', {student.Class}, '{student.Telephone}', '{student.Adress}')
        """
        try:
            self.cur.execute(sql)  # Выполнить запрос.
            self.con.commit()
        except sqlite3.DatabaseError as err:
            print("Error:", err)

    def add_students(self):
        n = int(input("Количество записей: "))
        for i in range(n):  # len(Students)):
            student = input("Student: ")
            Class = int(input("Class: "))
            telephone = input("Telephone: ")
            adress = input("adress: ")
            sql = f"""
            INSERT INTO Students(fio, class, telephone, address)
            VALUES ('{student}', {Class}, '{telephone}', '{adress}')
        """
            try:
                self.cur.execute(sql)  # Выполнить запрос.
                self.con.commit()
            except sqlite3.DatabaseError as err:
                print("Error:", err)

    def add_mark(self):
        sql = "INSERT INTO Marks(subject, mark, id_student) VALUES ('{subject}', {mark}, {id})"
        try:
            self.cur.execute(sql)  # Выполнить запрос.
            self.con.commit()
        except sqlite3.DatabaseError as err:
            print("Error:", err)


    def add_marks(self):
        l = int(input("Количество записей: "))
        for i in range(l):
            subject = input()
            mark = int(input())
            id = int(input())
            sql = f"""
            INSERT INTO Marks(subject, mark, id_student)
            VALUES ('{subject}', {mark}, {id})
        """
            try:
                self.cur.execute(sql)  # Выполнить запрос.
                self.con.commit()
            except sqlite3.DatabaseError as err:
                print("Error:", err)

    def list_students(self):
        print("Список учеников")
        sql = 'SELECT * FROM Students;'
        for stud in self.cur.execute(sql):
            print(stud)

    def list_marks(self):
        sql = """
        SELECT Marks.ROWID, fio, subject, mark FROM Students, Marks
        WHERE Students.id = Marks.id_student;
        """
        for stud in self.cur.execute(sql):
            print(stud)

    def del_students(self):
        dels = list(map(int, input('Строки для удаления: ').split()))
        for i in dels:
            sql = f"""
            DELETE FROM Students
            WHERE id={i};
            """
            self.cur.execute(sql)
        self.con.commit()

    def del_marks(self):
        dels = list(map(int, input('Строки для удаления: ').split()))
        for i in dels:
            sql = f"""
            DELETE FROM Marks
            WHERE ROWID={i};
            """
            self.cur.execute(sql)
        self.con.commit()

    def exit(self):
        self.cur.close()
        self.con.close()
