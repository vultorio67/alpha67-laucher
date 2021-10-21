# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'appQtDesigner.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1459, 856)
        MainWindow.setMaximumSize(QtCore.QSize(1459, 856))
        self.topwidget = QtWidgets.QWidget(MainWindow)
        self.topwidget.setObjectName("topwidget")
        self.pushButton = QtWidgets.QPushButton(self.topwidget)
        self.pushButton.setGeometry(QtCore.QRect(180, 120, 141, 41))
        self.pushButton.setMinimumSize(QtCore.QSize(141, 41))
        self.pushButton.setMaximumSize(QtCore.QSize(141, 41))
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.topwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1461, 851))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../../../../Downloads/Alpha67 Laucher.png"))
        self.label.setObjectName("label")
        self.comboBox_2 = QtWidgets.QComboBox(self.topwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(450, 750, 181, 41))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_3 = QtWidgets.QComboBox(self.topwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(110, 750, 181, 41))
        self.comboBox_3.setObjectName("comboBox_3")
        self.accounte = QtWidgets.QPushButton(self.topwidget)
        self.accounte.setGeometry(QtCore.QRect(20, 20, 121, 101))
        self.accounte.setText("")
        self.accounte.setObjectName("accounte")
        self.openFolder = QtWidgets.QPushButton(self.topwidget)
        self.openFolder.setGeometry(QtCore.QRect(770, 750, 181, 41))
        self.openFolder.setObjectName("openFolder")
        self.play = QtWidgets.QPushButton(self.topwidget)
        self.play.setGeometry(QtCore.QRect(1190, 680, 181, 81))
        self.play.setObjectName("play")
        self.ram = QtWidgets.QLCDNumber(self.topwidget)
        self.ram.setGeometry(QtCore.QRect(1210, 500, 141, 41))
        self.ram.setObjectName("ram")
        self.cpu = QtWidgets.QLCDNumber(self.topwidget)
        self.cpu.setGeometry(QtCore.QRect(1210, 210, 141, 41))
        self.cpu.setObjectName("cpu")
        MainWindow.setCentralWidget(self.topwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "play"))
        self.openFolder.setText(_translate("MainWindow", "ouvrir le dossier minecraft"))
        self.play.setText(_translate("MainWindow", "Play"))
