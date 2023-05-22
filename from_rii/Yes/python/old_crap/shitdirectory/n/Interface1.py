import tkinter as tk
# Подключить модуль для работы с диалоговыми окнами.
from tkinter import messagebox as mb

from StudDB import *
from Student_form import *

class Interface:
    def __init__(self, form):
        self.form = form
        # Задать заголовок и размеры окна.
        self.form.title("Данные об учащихся")
        self.form.geometry("500x400+300+200")

        # Создать экземпляр класса Reports().
        self.students_data = StudentsDB()
        self.set_menu()

    def set_menu(self):
        """
        Формирование главного меню окна.
        """
        # Создать объект Меню на форме.
        form_menu = tk.Menu(self.form)
        # Конфигурировать окно с указанием меню для него.
        self.form.config(menu=form_menu)
        # Создать пункт меню с размещением на основном меню.
        pm1 = tk.Menu(form_menu)
        # Создать подменю для пункта "Таблицы".
        form_menu.add_cascade(label="Таблицы", menu=pm1)
        # Сформировать список команд пункта меню:
        # добавить пункт подменю с указанием команды,
        pm1.add_command(label="Добавить",
                        command=self.students_data.create_table)
        # команда - это метод класса Student().
        pm1.add_command(label="Изменить")
        pm1.add_command(label="Удалить")

        # Добавить второй пункт меню.
        pm2 = tk.Menu(form_menu)
        # Добавить пункты подменю.
        form_menu.add_cascade(label="Редактирование данных", menu=pm2)
        # Сформировать список команд пункта меню:
        # добавить пункт подменю с указанием команды,
        pm2_1 = tk.Menu(pm2)
        pm2.add_cascade(label="Консоль", menu=pm2_1)
        pm2_1.add_command(label="Учащиеся",
                        command=self.students_data.add_students)
        pm2_1.add_command(label="Оценки",
                        command=self.students_data.add_marks)
        pm2_2 = tk.Menu(pm2)
        pm2.add_cascade(label="Формы", menu=pm2_2)

        pm2_2.add_command(label="Данные об учащихся",
                        command=self.new_win_stud)
        pm2_2.add_command(label="Добавить учащегося",
                          command=self.new_win_add_stud)
        pm2_2.add_command(label="Добавить оценки",
                        command=self.new_win_add_mark)

        pm3 = tk.Menu(form_menu)  # Третий пункт меню.
        form_menu.add_cascade(label="Поиск и фильтрация", menu=pm3)
        pm3.add_command(label="По критериям...")

        # Четвертый пункт меню не будет содержать вложенных подпунктов.
        form_menu.add_cascade(label="Выход", command=self.close_win)

    def new_win_stud(self):
        """
        Создание нового окна с элементами управления.
        Вызывается из главного окна.
        """
        Student_edit(self.form, self.students_data)
        # form = tk.Toplevel(self.form)
        # # Задать заголовок и размеры окна.
        # form.title("Добавление данных об учащемся")
        # form.geometry("400x400+150+200")
        #
        # tk.Button(form, text="Добавить", command=create).pack(pady=10)
        # tk.Button(form, text="Отменить", command=form.destroy).pack(pady=10)

    def new_win_add_stud(self):
        """
        Создание нового окна с элементами управления.
        Вызывается из главного окна.
        """
        form = tk.Toplevel(self.form)
        # Задать заголовок и размеры окна.
        form.title("Добавление данных об учащемся")
        form.geometry("400x400+150+200")
        # Создать виджеты окна.
        tk.Label(form, text="Введите ФИО", height=3).pack()
        entry1 = tk.Entry(form)
        entry1.pack()
        tk.Label(form, text="Введите класс", height=3).pack()
        entry2 = tk.Entry(form)
        entry2.pack()
        tk.Label(form, text="Введите телефон", height=3).pack()
        entry3 = tk.Entry(form)
        entry3.pack()
        tk.Label(form, text="Введите адрес", height=3).pack()
        entry4 = tk.Entry(form)
        entry4.pack()
        # Задать лябда-функцию, которая будет выполняться
        # при нажатии на кнопку 'Добавить'.
        # Если ФИО или класс не введены,
        # вызвать диалоговое окно ошибки.
        create = lambda: mb.showerror("Ошибка", "Данные отсутствуют!") \
            if entry1.get() == "" or entry2.get() == "" else \
            self.students_data.add_student(Student(entry1.get(), (entry2.get()),
                                                   entry3.get(), entry4.get()))

        # entry1.get() - Получить данные из поля.

        tk.Button(form, text="Добавить", command=create).pack(pady=10)
        tk.Button(form, text="Отменить", command=form.destroy).pack(pady=10)

    def new_win_add_mark(self):
        """
        Создание нового окна с элементами управления.
        Вызывается из главного окна.
        """
        form = tk.Toplevel(self.form)
        # Задать заголовок и размеры окна.
        form.title("Добавление данных об учащемся")
        form.geometry("400x400+150+200")
        # Создать виджеты окна.
        tk.Label(form, text="Введите ФИО", height=3).pack()
        entry1 = tk.Entry(form)
        entry1.pack()
        tk.Label(form, text="Введите класс", height=3).pack()
        entry2 = tk.Entry(form)
        entry2.pack()
        tk.Label(form, text="Введите телефон", height=3).pack()
        entry3 = tk.Entry(form)
        entry3.pack()
        tk.Label(form, text="Введите адрес", height=3).pack()
        entry4 = tk.Entry(form)
        entry4.pack()
        # Задать лябда-функцию, которая будет выполняться
        # при нажатии на кнопку 'Добавить'.
        # Если ФИО или класс не введены,
        # вызвать диалоговое окно ошибки.
        create = lambda: mb.showerror("Ошибка", "Данные отсутствуют!") \
            if entry1.get() == "" or entry2.get() == "" else \
            self.students_data.add_student(Student(entry1.get(), (entry2.get()),
                                                   entry3.get(), entry4.get()))

        # entry1.get() - Получить данные из поля.

        tk.Button(form, text="Добавить", command=create).pack(pady=10)
        tk.Button(form, text="Отменить", command=form.destroy).pack(pady=10)

    def close_win(self):
        """
        Действия при завершении работы с программой.
        Вызов диалогового окна.
        """
        answer = mb.askyesno(title="Выход", message="Завершить работу?")
        if answer: # == True
            self.students_data.exit()
            self.form.destroy()

