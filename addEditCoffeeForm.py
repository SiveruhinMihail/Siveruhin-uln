# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


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
