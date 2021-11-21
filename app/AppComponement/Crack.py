import os
import time

import minecraft_launcher_lib
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from PyQt5 import QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (QMainWindow)

import sys
sys.path.append("..")
from AppGraphic.CrackLogin import Ui_Form
import json
import encrypte


def __init__():
    user = os.getlogin()
    print("ok")
    mla = QtWidgets.QWidget()
    uia = Ui_Form()
    uia.setupUi(mla)
    mla.show()

    def upass():
        try:
            with open("C:/Users/" + user + "\AppData\Roaming\.alpha67/alpha/cred.json", "r") as jsonFile:
                data = json.load(jsonFile)

            data["crack"][0]['username'] = str(uia.lineEdit.text())
            print(data["crack"][0]['username'])

            with open("C:/Users/" + user + "\AppData\Roaming\.alpha67/alpha/cred.json", "w") as jsonFile:
                json.dump(data, jsonFile)

            with open("C:/Users/" + user + "\AppData\Roaming\.alpha67/alpha/select.json", "r") as jsonFile:
                data = json.load(jsonFile)
                print(data)

            data["crack"][0]["connect"] = "True"
            data["crack"][0]["select"] = "True"
            data["microsoft"][0]["select"] = "False"
            data["mojang"][0]["select"] = "False"
            print(data)

            with open("C:/Users/" + user + "\AppData\Roaming\.alpha67/alpha/select.json", "w") as jsonFile:
                json.dump(data, jsonFile)

            mla.close()

        except:
            None

    uia.pushButton.clicked.connect(upass)