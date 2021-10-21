# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'appQtButton.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        super().__init__()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(487, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mojang = QtWidgets.QPushButton(self.centralwidget)
        self.mojang.setGeometry(QtCore.QRect(130, 130, 221, 51))
        self.mojang.setObjectName("mojang")
        self.micro = QtWidgets.QPushButton(self.centralwidget)
        self.micro.setGeometry(QtCore.QRect(130, 280, 221, 51))
        self.micro.setObjectName("micro")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(130, 420, 221, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 501, 601))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../img/login Button.jpg"))
        self.label.setObjectName("label")
        self.label.raise_()
        self.mojang.raise_()
        self.micro.raise_()
        self.pushButton_3.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.mojang.setText(_translate("MainWindow", "Mojang Login"))
        self.micro.setText(_translate("MainWindow", "Microsoft Login"))
        self.pushButton_3.setText(_translate("MainWindow", "Crack Login"))
