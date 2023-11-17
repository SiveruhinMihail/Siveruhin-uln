import sys
import sqlite3

from PyQt5.QtWidgets import QWidget, QApplication, QTableWidget, QMainWindow, QTableWidgetItem
from PyQt5.QtWidgets import QPushButton
from PyQt5 import uic


class coffee(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.setWindowTitle('Expresso')
        with sqlite3.connect('coffee.sqlite') as db:
            cur = db.cursor()
            result = list(cur.execute(f'select * from espresso'))
            self.tableWidget.setColumnCount(len(result[0]))
            self.titles = [description[0] for description in cur.description]
            self.tableWidget.setRowCount(len(result))

            for i, elem in enumerate(result):
                for j, val in enumerate(elem):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))

        self.add.clicked.connect(self.add1)
        self.edit.clicked.connect(self.edit1)

    def add1(self):
        self.window1 = Espress2()
        self.window1.show()

        self.close()

    def edit1(self):
        rows = list(set([i.row() for i in self.tableWidget.selectedItems()]))
        if rows:
            self.window1 = Espress2(n=1, row=rows[0] + 1)
            self.window1.show()

            self.close()


class Espress2(QMainWindow):
    def __init__(self, n=0, row=0):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.rows = row
        if n == 0:
            self.pushButton.clicked.connect(self.save)
        else:
            self.pushButton.setText('edit')
            self.pushButton.clicked.connect(self.save)

    def save(self):
        if self.sender().text() == 'add':
            with sqlite3.connect('coffee.sqlite') as db:
                cur = db.cursor()
                result = cur.execute(
                    """insert into espresso(название_сорта, степень_обжарки, молотый, описание_вкуса, цена, объем_упаковки) values(?, ?, ?, ?, ?, ?)""",
                    (self.namesorts.text(), self.degree.text(), self.molot.text(), self.description.text(),
                     self.price.text(),
                     self.allV.text()))
        else:
            with sqlite3.connect('coffee.sqlite') as db:
                cur = db.cursor()
                result = cur.execute(
                    """update espresso set название_сорта = ?, степень_обжарки = ?, молотый = ?, описание_вкуса = ?, цена = ?, объем_упаковки = ? where ID = ?""",
                    (self.namesorts.text(), self.degree.text(), self.molot.text(), self.description.text(),
                     self.price.text(),
                     self.allV.text(), self.rows))
        self.window1 = coffee()
        self.window1.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = coffee()
    ex.show()
    sys.exit(app.exec())
