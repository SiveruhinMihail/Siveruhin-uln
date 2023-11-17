import sys
import sqlite3

from PyQt5.QtWidgets import QWidget, QApplication, QTableWidget, QMainWindow, QTableWidgetItem
from PyQt5 import uic


class coffee(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.setWindowTitle('Expresso')
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        result = list(cur.execute(f'select * from espresso'))
        self.tableWidget.setColumnCount(len(result[0]))
        self.titles = [description[0] for description in cur.description]
        self.tableWidget.setRowCount(len(result))

        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = coffee()
    ex.show()
    sys.exit(app.exec())
