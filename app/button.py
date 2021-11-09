# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'button.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(411, 463)
        self.microsoft = QtWidgets.QPushButton(Form)
        self.microsoft.setGeometry(QtCore.QRect(130, 260, 151, 61))
        self.microsoft.setObjectName("microsoft")
        self.crack = QtWidgets.QPushButton(Form)
        self.crack.setGeometry(QtCore.QRect(130, 380, 151, 61))
        self.crack.setObjectName("crack")
        self.mojang = QtWidgets.QPushButton(Form)
        self.mojang.setGeometry(QtCore.QRect(130, 130, 151, 61))
        self.mojang.setObjectName("mojang")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 411, 471))
        self.label.setMaximumSize(QtCore.QSize(411, 471))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../img/login Button.jpg"))
        self.label.setObjectName("label")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(100, 150, 16, 20))
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(Form)
        self.checkBox_2.setGeometry(QtCore.QRect(100, 280, 16, 20))
        self.checkBox_2.setText("")
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(Form)
        self.checkBox_3.setGeometry(QtCore.QRect(100, 400, 16, 20))
        self.checkBox_3.setText("")
        self.checkBox_3.setObjectName("checkBox_3")
        self.label.raise_()
        self.microsoft.raise_()
        self.crack.raise_()
        self.mojang.raise_()
        self.checkBox.raise_()
        self.checkBox_2.raise_()
        self.checkBox_3.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.microsoft.setText(_translate("Form", "Microsoft Login"))
        self.crack.setText(_translate("Form", "Crack Login"))
        self.mojang.setText(_translate("Form", "Mojang Login"))
