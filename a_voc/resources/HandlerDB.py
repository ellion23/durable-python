import sqlite3


class HandlerDB():
    def return_values(self):
        for row in cur.execute('SELECT * FROM Words'):
            return row


con = sqlite3.connect('/home/ellion/PycharmProjects/pythonProject/_voc/resources/my_vocabulary.db')
cur = con.cursor()


