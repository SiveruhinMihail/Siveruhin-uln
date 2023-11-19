import sys
import sqlite3

from PyQt5.QtWidgets import QWidget, QApplication, QTableWidget, QMainWindow, QTableWidgetItem
from PyQt5.QtWidgets import QPushButton
from PyQt5 import uic, QtWidgets, QtCore


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(30, 30, 341, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.add = QtWidgets.QPushButton(Form)
        self.add.setGeometry(QtCore.QRect(280, 240, 93, 28))
        self.add.setObjectName("add")
        self.edit = QtWidgets.QPushButton(Form)
        self.edit.setGeometry(QtCore.QRect(30, 240, 93, 28))
        self.edit.setObjectName("edit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.add.setText(_translate("Form", "add"))
        self.edit.setText(_translate("Form", "edit"))

class Ui_Form1(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 20, 111, 16))
        self.label.setObjectName("label")
        self.namesorts = QtWidgets.QLineEdit(Form)
        self.namesorts.setGeometry(QtCore.QRect(120, 20, 251, 22))
        self.namesorts.setObjectName("namesorts")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 171, 16))
        self.label_2.setObjectName("label_2")
        self.degree = QtWidgets.QSpinBox(Form)
        self.degree.setGeometry(QtCore.QRect(190, 50, 42, 22))
        self.degree.setMaximum(100)
        self.degree.setObjectName("degree")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 111, 16))
        self.label_3.setObjectName("label_3")
        self.molot = QtWidgets.QSpinBox(Form)
        self.molot.setGeometry(QtCore.QRect(120, 80, 42, 22))
        self.molot.setMaximum(1)
        self.molot.setObjectName("molot")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(20, 110, 111, 16))
        self.label_4.setObjectName("label_4")
        self.description = QtWidgets.QLineEdit(Form)
        self.description.setGeometry(QtCore.QRect(120, 110, 251, 22))
        self.description.setObjectName("description")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(20, 140, 111, 16))
        self.label_5.setObjectName("label_5")
        self.price = QtWidgets.QLineEdit(Form)
        self.price.setGeometry(QtCore.QRect(120, 140, 251, 22))
        self.price.setObjectName("price")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(20, 170, 111, 16))
        self.label_6.setObjectName("label_6")
        self.allV = QtWidgets.QLineEdit(Form)
        self.allV.setGeometry(QtCore.QRect(120, 170, 251, 22))
        self.allV.setObjectName("allV")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(280, 240, 93, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "название сорта"))
        self.label_2.setText(_translate("Form", "степень прожарки (0, 100)"))
        self.label_3.setText(_translate("Form", "Молотый да/нет"))
        self.label_4.setText(_translate("Form", "описание вкуса"))
        self.label_5.setText(_translate("Form", "Цена"))
        self.label_6.setText(_translate("Form", "объем"))
        self.pushButton.setText(_translate("Form", "add"))

class coffee(QMainWindow, Ui_Form):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle('Expresso')
        with sqlite3.connect('data/coffee.sqlite') as db:
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


class Espress2(QMainWindow, Ui_Form1):
    def __init__(self, n=0, row=0):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.rows = row
        if n == 0:
            self.pushButton.clicked.connect(self.save)
        else:
            self.pushButton.setText('edit')
            self.pushButton.clicked.connect(self.save)

    def save(self):
        if self.sender().text() == 'add':
            with sqlite3.connect('data/coffee.sqlite') as db:
                cur = db.cursor()
                result = cur.execute(
                    """insert into espresso(название_сорта, степень_обжарки, молотый, описание_вкуса, цена, объем_упаковки) values(?, ?, ?, ?, ?, ?)""",
                    (self.namesorts.text(), self.degree.text(), self.molot.text(), self.description.text(),
                     self.price.text(),
                     self.allV.text()))
        else:
            with sqlite3.connect('data/coffee.sqlite') as db:
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
