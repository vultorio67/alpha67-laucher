import json
import urllib.request
import time
import os
import shutil
from colorama import Fore, Back, Style
from datetime import date, datetime
from ast import literal_eval
import tkinter
from tkinter import filedialog
from win10toast_click import ToastNotifier
import glob
import threading
import psutil
from PyQt5 import QtCore, QtGui, QtWidgets
#from PyQt5.uic.properties import QtCore, QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

from PyQt5.QtCore import QDir, Qt, QUrl, QPropertyAnimation
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (QMainWindow, QWidget, QPushButton, QApplication,
                             QLabel, QFileDialog, QStyle, QVBoxLayout)

# GUI FILE
from appQtDesigner import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import QDir, Qt, QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (QMainWindow, QWidget, QPushButton, QApplication,
                             QLabel, QFileDialog, QStyle, QVBoxLayout)

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import subprocess

import qdarkstyle
import os

from qt_material import apply_stylesheet

import minecraft_launcher_lib
from button import Ui_Form

os.environ['QT_API'] = 'pyqt5'


class MainWindow(QMainWindow):

    @pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')

    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.saidbis = None


        #self.setWindowTitle("")

        # setting window icon
        self.setWindowIcon(QIcon("../img/bg1.png"))

        # setting icon text
        self.setWindowIconText("logo")

        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        videoWidget = QVideoWidget()
        self.ui.setupUi(self)

        self.ui.comboBox_3.addItem("Valilla")
        self.ui.comboBox_3.addItem("Forge")

        self.w = None

        self.ui.openFolder.clicked.connect(self.openFolder)
        self.ui.accounte.clicked.connect(self.Window2)

        self.ui.comboBox_2.addItem("Alpha67-server")

        self.minecraft_directory = minecraft_launcher_lib.utils.get_minecraft_directory()
        for i in minecraft_launcher_lib.utils.get_available_versions(self.minecraft_directory):
            # Only add release versions
            if i["type"] == "release":
                self.ui.comboBox_2.addItem(i["id"])
                #self.version_select.addItem(i["id"])

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../img/connect logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ui.accounte.setIcon(icon)
        self.ui.accounte.setIconSize(QtCore.QSize(121, 101))

        self.ui.accounte.setStyleSheet("QPushButton::hover"
                                           "{"
                                           "background-color : Bisque;"
                                           "}"
                                           )



        self.ui.label.setPixmap(QtGui.QPixmap("../img/Alpha67 Laucher.png"))
        self.mediaPlayer.setMedia(
            QMediaContent(QUrl.fromLocalFile('Alpha67.avi')))
        self.hello()

#        self.ui.pushButton.clicked.connect(self.play)
        self.mediaPlayer.setVideoOutput(videoWidget)
        self.show()

    def openFolder(self):
        print("open alpha folder")
        # subprocess.Popen('explorer "C:/Users\evanm\.VirtualBox"')
        #subprocess.call('start C:/Users\%username%\AppData\Roaming\.alpha67\minecraft')
        os.system('cmd /c "start C:/Users\%username%\AppData\Roaming\.alpha67\minecraft"')

    def play(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

    def hello(self):
        th1 = threading.Thread(target=self.smart)
        th1.start()
        th2 = threading.Thread(target=self.updateApp)
        th2.start()
        print("sa")


    def smart(self):
        print("ok")

    def updateApp(self):
        print("100")
        while True:
            self.ui.cpu.display(str(psutil.cpu_percent(4)))
            dict(psutil.virtual_memory()._asdict())
            # you can have the percentage of used RAM
            ram = psutil.virtual_memory().percent
            self.ui.ram.display(str(ram))



    def resizeMainWindow(self, width, height):
        # CREATE ANIMATION
        self.animation = QPropertyAnimation(self, b"size")
        self.animation.setDuration(1000)
        self.animation.setEndValue(QtCore.QSize(width,height))
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
        self.animation.start()

    def Window2(self):
        self.Form = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.Form)
        self.Form.show()



class AnotherWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Another Window")
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.resize(487, 600)











if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())