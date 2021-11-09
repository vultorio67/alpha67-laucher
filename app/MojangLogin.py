# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MojangLogin.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 438)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(70, 170, 261, 31))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 260, 261, 31))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(132, 347, 131, 51))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 401, 441))
        self.label.setMaximumSize(QtCore.QSize(401, 441))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../img/login-background.jpg"))
        self.label.setObjectName("label")
        self.info = QtWidgets.QLabel(Form)
        self.info.setGeometry(QtCore.QRect(90, 310, 221, 20))
        self.info.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.info.setText("")
        self.info.setAlignment(QtCore.Qt.AlignCenter)
        self.info.setObjectName("info")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 40, 281, 61))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../img/Mojang-Log.png"))
        self.label_2.setObjectName("label_2")
        self.label.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.pushButton.raise_()
        self.info.raise_()
        self.label_2.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Username"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "password"))
        self.pushButton.setText(_translate("Form", "Login"))
