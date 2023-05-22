import tkinter as tk
from RussianDatabase import *
from tkinter import messagebox as mb

class Interface:
    def __init__(self, form):
        self.form  = form
        # Задать заголовок и размеры окна.
        self.form.title("Russian's private info for American agents")
        self.form.geometry("500x400+300+200")
        # Создать экземпляр класса StudentsDB()
        self.students_data = RussianDatabase()
        self.set_menu()

    def set_menu(self):
        """
        Формирование главного меню.
        """
        # Создать объект Меню на форме.
        form_menu = tk.Menu(self.form)
        # Конфигурировать окно с указанием меню для него.
        self.form.config(menu=form_menu)

        # Создать пункт меню с размещением на основном меню.
        pm1 = tk.Menu(form_menu)
        # Создать подменю для пункта "Таблицы".
        form_menu.add_cascade(label="Tables", menu=pm1)
        # Сформировать список команд пункта меню:
        # добавить пункт подменю с указанием команды,
        pm1.add_command(label="Create tables", command=self.students_data.create_table)
            # команда - это метод класса Student().
        pm1.add_command(label="Edit")
        pm1.add_command(label="Delete")

        # Добавить второй пункт меню.
        pm2 = tk.Menu(form_menu)
        # Добавить пункты подменю.
        form_menu.add_cascade(label="Data edit", menu=pm2)
        # Сформировать список команд пункта меню:
        # добавить пункт подменю с указанием команды,
        pm2.add_command(label="Add russian info", command=self.students_data.add)
        pm2.add_command(label="Delete", command=self.students_data.delete)      # не работает :(
        pm2.add_command(label="What is it?", command=self.new_win)      # Показывает, но не работает :)
        # pm3 = tk.Menu(form_menu)    # Третий пункт меню.
        # form_menu.add_cascade(label="...", menu=pm3)
        form_menu.add_cascade(label="Exit", command=self.close_win)

    def close_win(self):
        answer = mb.askyesno(title="Exit", message="Are you sure?")
        if answer == True:
            self.students_data.exit()
            self.form.destroy()

    def new_win(self):
        """
        Создание нового окна с элементами управления.
        Вызывается из глобального окна
        Пока это заготовка, но когда-нибудь будет работать (но окошко выводит).... :D
        """
        form = tk.Toplevel(self.form)
        # Задать заголовок и размеры окна.
        form.title("Добавление данных об учащемся")
        form.geometry("400x400+150+300")

        # Создать виджеты окна.
        tk.Label(form, text="Napishite tablitsa_name", height=3).pack()
        entry0 = tk.Entry(form)
        entry0.pack(pady=10)
        tk.Label(form, text="Napishite ФИО", height=3).pack()
        entry1 = tk.Entry(form)
        entry1.pack(pady=10)
        tk.Label(form, text="Vvedite class", height=3).pack()
        entry2 = tk.Entry(form)
        entry2.pack(pady=10)
        # tk.Label(form, text=)

        tk.Button(form, text="Add new info", command=RussianDatabase.add(entry0)).pack(pady=10)
        tk.Button(form, text="Cancel", command=form.destroy).pack(pady=10)
