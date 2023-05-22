import sys
from PyQt5 import *
from PyQt5 import QtSql
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtWidgets import QApplication, QMessageBox, QLabel

con = QSqlDatabase.addDatabase("QSQLITE")
con.setDatabaseName("my_vocabulary.db")

app = QApplication(sys.argv)

if not con.open():
    QMessageBox.critical(
        None,
        "App Name - Error!",
        "Database Error: %s" % con.lastError().databaseText(),
    )
    sys.exit(1)

print(con.tables())





win = QLabel("Connection Successfully Opened!")
win.setWindowTitle("Notifcation")
win.resize(400, 300)
win.show()
sys.exit(app.exec_())