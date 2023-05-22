import sys
# import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from PyQt5.QtGui import QIcon
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QTableWidget,
    QTableWidgetItem,
)
from ui import Ui_MainWindow
from WLWindow import Ui_WList
from WTWindow import Ui_WTable


class MyProg(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyProg, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle('App for DB')
        self.setWindowIcon(QIcon('resources/icon.png'))
    #     self.ui.InputLine1.setPlaceholderText('Введите число:')
    #     self.ui.ButtonPlus.clicked.connect(self.plus)
        self.ui.BShowWords.clicked.connect(self.print_words_list)
        self.ui.BShowTables.clicked.connect(self.database_list)
        self.ui.actionWords.triggered.connect(self.openTableWindow)
        # connect(self.openTableWindow)

    # def database_list(self):
    #     stm = QtSql.QSqlTableModel()
    #     stm.setTable('Words')
    #     cur.execute('SELECT name from sqlite_master where type= "table"')
    #     self.ui.OutputBlock.append(str(cur.fetchall()))
    def database_list(self):
        self.ui.OutputBlock.append(str(con.tables()))


    # def print_words_list(self):
    #     for value in return_values():
    #         self.ui.OutputBlock.append(str(value))

    def print_words_list(self):
        que = QSqlQuery()
        que.exec('SELECT "English", "Перевод", "Транскрипция", "Словосочетания" FROM Words')
        while que.next():
            self.ui.OutputBlock.append(que.value(0))
        que.finish()

    def openTableWindow(self):
        self.TableW = TableW()
        self.TableW.show()


class TableW(QtWidgets.QListWidget):
    def __init__(self):
        super(TableW, self).__init__()
        self.WTWindow = Ui_WTable()
        self.WTWindow.setupUi(self)
        self.inUI()
        # Set up the view and load the data
        # self.view = self.WTWindow.WordsTable
        self.WTWindow.WordsTable.setHorizontalHeaderLabels(["English", "Перевод", "Транскрипция"])
        query = QSqlQuery('SELECT "English", "Перевод", "Транскрипция" FROM "Words"')
        while query.next():
            rows = self.WTWindow.WordsTable.rowCount()
            self.WTWindow.WordsTable.setRowCount(rows + 1)
            self.WTWindow.WordsTable.setItem(rows, 0, QTableWidgetItem(str(query.value(0))))
            self.WTWindow.WordsTable.setItem(rows, 1, QTableWidgetItem(query.value(1)))
            self.WTWindow.WordsTable.setItem(rows, 2, QTableWidgetItem(query.value(2)))
            self.WTWindow.WordsTable.setItem(rows, 3, QTableWidgetItem(query.value(3)))
        self.WTWindow.WordsTable.resizeColumnsToContents()

    def inUI(self):
        self.setWindowTitle('Table Words')


# def return_values():
#     g = []
#     for row in cur.execute('SELECT * FROM Words'):
#         g.append(row)
#     return g


con = QtSql.QSqlDatabase.addDatabase('QSQLITE')
con.setDatabaseName('resources/my_vocabulary.db')
con.open()
# con = sqlite3.connect('/home/ellion/PycharmProjects/pythonProject/_voc/resources/my_vocabulary.db')
# cur = con.cursor()

# cur.execute('SELECT name from sqlite_master where type= "table"')
# cur.fetchall()

app = QtWidgets.QApplication([])
application = MyProg()
application.show()

# for g in cur.execute('SELECT * FROM Words'):
#     print(g)
# print(return_values())
# for i in return_values():
#     print(i)
sys.exit(app.exec())
# cur.close()

