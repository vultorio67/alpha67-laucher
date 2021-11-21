import os
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
from AppGraphic.MojangLogin import Ui_Form as ml
import json
import encrypte


def __init__():
    mla = QtWidgets.QWidget()
    uia = ml()
    uia.setupUi(mla)
    mla.show()

    def upass():
        user = os.getlogin()
        userName = uia.lineEdit.text()
        password = uia.lineEdit_2.text()

        userName = str(userName)
        password = str(password)

        login_data = minecraft_launcher_lib.account.login_user(userName, password)

        userName = userName.replace("'", "")
        password = password.replace("'", "")

        userName = userName.replace("b", "")
        password = password.replace("b", "")

        try:
            print(login_data['error'])
            uia.info.setText("mot de pass ou identifiant invalide !")

        except:
            print("True login")
            uia.info.setText("Identification reussi =)")
            passwordEnc = str(user + "67")
            userName = encrypte.password_encrypt(userName.encode(), passwordEnc)
            password = encrypte.password_encrypt(password.encode(), passwordEnc)

            def crack():
                try:
                    with open('C:/Users/' + user + '\AppData\Roaming\.alpha67/alpha/cred.json', 'r') as file:
                        uInfo = json.load(file)
                        # uInfo = literal_eval(uInfo)

                        uInfo = uInfo['crack']
                        uInfo = uInfo[0]
                        print(uInfo)
                        uInfo = uInfo['username']
                        print(uInfo)
                        return uInfo
                except:
                    return None

            x = {

                "mojang": [
                    {"username": str(userName), "password": str(password)}
                ],
                "crack": [
                    {"username": crack()}
                ]
            }

            with open('C:/Users/' + user + '\AppData\Roaming\.alpha67/alpha/cred.json', 'w') as outfile:
                json.dump(x, outfile)

            with open("C:/Users/" + user + "\AppData\Roaming\.alpha67/alpha/select.json", "r") as jsonFile:
                data = json.load(jsonFile)
                print(data)

            data["mojang"][0]["connect"] = "True"
            data["mojang"][0]["select"] = "True"
            data["microsoft"][0]["select"] = "False"
            data["crack"][0]["select"] = "False"
            print(data)

            with open("C:/Users/" + user + "\AppData\Roaming\.alpha67/alpha/select.json", "w") as jsonFile:
                json.dump(data, jsonFile)

            mla.close()

    uia.pushButton.clicked.connect(upass)