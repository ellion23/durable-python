import tkinter as tk
from StudDB import *


class Student_edit:
    """
    Класс создания интерфейса окна.
    """

    def __init__(self, form, students_data):
        self.form = tk.Toplevel(form)
        self.form.title("Учащиеся")
        self.form.geometry("1000x600")
        self.students_data = students_data
        self.keys = ["id", "fio", "class", "telephone", "address"]
        self.widgets()
        self.select()

    def select(self):
        n = self.var.get()
        sql = "SELECT * FROM Students"
        if self.entry[5].get() == "":
            sql += ';'
        else:
            sql += " WHERE " + self.keys[n] + " = "
            if n in (0, 2):
                sql += self.entry[5].get() + ";"
            else:
                sql += "'" + self.entry[5].get() + "';"
        self.list_students = list(self.students_data.cur.execute(sql))

        self.index = 0
        self.count = len(self.list_students)
        self.display()
    def display(self):
        for i in range(5):
            self.entry[i].delete(0, tk.END)
        if self.count:
            for i in range(5):
                self.entry[i].insert(0, str(self.list_students[self.index][i]))
            self.text.delete(0.0, tk.END)

            sql = "SELECT subject, mark FROM Marks WHERE id_student = "
            sql += str(self.list_students[self.index][0]) + ";"
            k = s = 0
            print(sql)
            for mark in self.students_data.cur.execute(sql):
                print(mark)
                self.text.insert(0.0, f"{mark[0]}  {mark[1]}\n")
                k += 1
                s += mark[1]
            self.entry[6].delete(0, tk.END)
            if k:
                    self.entry[6].insert(0, str(s / k))
    def next(self):
        if self.index < self.count-1:
            self.index += 1
        self.display()

    def prev(self):
        if self.index > 0:
            self.index -= 1
        self.display()
    def widgets(self):
        # Добавление виджетов на форму.
        # grid - упаковщик (размещает данные в виде таблицы).
        tk.Label(self.form, text="Данные об учащихся", font="20").grid(row=0, column=1)
        # Создание списка текстовых полей.
        self.entry = [0] * 9
        # Создание списка подписей (меток).
        label = ["Код", "ФИО", "Класс", "Телефон", "Адрес"]
        for i in range(5):
            tk.Label(self.form, text=label[i], font="20").grid(row=1, column=i, padx=5)
            self.entry[i] = tk.Entry(self.form, font="Arial 12")
            self.entry[i].grid(row=2, column=i, padx=5)

        # Метка нужна для разделения данных на форме.
        tk.Label(self.form).grid(row=3, column=1)
        # Добавление кнопок на форму.
        self.button_change = self.do_button(4, 1, "Изменить", self.change_student)
        self.button_prev = self.do_button(4, 2, "Назад", self.prev)
        self.button_next = self.do_button(4, 3, "Далее", self.next)
        # Метка для разделения данных на форме.
        tk.Label(self.form).grid(row=6, column=1)
        tk.Label(self.form, text="Оценки учащегося", font="20").grid(row=7, column=1)

        # Многострочный вывод текста.
        self.text = tk.Text(self.form, height=20, width=60, font="Arial 12", wrap=tk.WORD)
        self.text.grid(row=8, column=0, columnspan=3)

        # Задать критерии для вывода данных из БД.
        tk.Label(self.form, text="Задайте критерий", font="20").grid(row=7, column=3)
        self.var = tk.IntVar()
        # var.set(1)
        p = tk.Frame(self.form, width=200, height=300)
        p.grid(row=8, column=3, sticky=tk.N, pady=20)
        self.rad = [0] * 4
        for i in range(4):
            self.rad[i] = tk.Radiobutton(p, text=label[i],
                                         variable=self.var, value=i, font="20")
            self.rad[i].pack(side=tk.TOP, anchor=tk.W)

        self.entry[5] = tk.Entry(self.form, font="Arial 12")
        self.entry[5].grid(row=8, column=3, sticky=tk.S, pady=150)
        self.button_select = tk.Button(self.form, text="Выполнить", font="Arial 12",
                                       command=self.select)
        self.button_select.grid(row=8, column=3, sticky=tk.S, pady=50)
        self.var.set(0)

        tk.Label(self.form, text="Средний балл", font="20").grid(row=9, column=1)
        self.entry[6] = tk.Entry(self.form, font="Arial 12")
        self.entry[6].grid(row=9, column=2)

        tk.Label(self.form, text="Добавление оценок", font="20").grid(row=10, column = 0)
        tk.Label(self.form, text="Предмет", font="20").grid(row=11, column = 0)
        self.entry[7] = tk.Entry(self.form, font="Arial 12")
        self.entry[7].grid(row=12, column=0)

        tk.Label(self.form, text="Оценка", font="20").grid(row=11, column=1)
        self.entry[8] = tk.Entry(self.form, font="Arial 12")
        self.entry[8].grid(row=12, column=1)
        self.button_mark_apply = self.do_button(12, 2, "Припять", self.add_mark)
    def do_button(self, row, column, text, func):
        # Метод для формирования кнопок.
        button = tk.Button(self.form, text=text, font="Arial 12", command=func)
        button.grid(row=row, column=column, padx=15)
        return button

    def change_student(self):
        sql = "UPDATE Students SET "
        for i in range(1, 5):
            sql += self.keys[i] + " = "
            if i == 2:
                sql += self.entry[i].get()
            else:
                sql += "'" + self.entry[i].get() + "'"
            if i != 4:
                sql += ", "

        sql += "WHERE " + self.keys[0] + " = " + self.entry[0].get()
        sql += ";"
        self.students_data.cur.execute(sql)
        self.students_data.con.commit()
        self.select()

    def add_mark(self):
        subject = self.entry[7].get()
        mark = self.entry[8].get()
        self.students_data.add_mark(subject, mark, self.entry[0].get())