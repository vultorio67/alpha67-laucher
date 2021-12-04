import json
import time
#from win10toast_click import ToastNotifier
import threading
import psutil
from PyQt5 import QtCore, QtGui
#from PyQt5.uic.properties import QtCore, QtGui
from PyQt5 import QtWidgets
import sys
import encrypte

from PyQt5.QtCore import QPropertyAnimation

# GUI FILE
from AppGraphic.appQtDesigner import Ui_MainWindow
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (QMainWindow)

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import os
import uuid
import subprocess

from qt_material import apply_stylesheet

import minecraft_launcher_lib

#from the laucher
from AppGraphic.button import Ui_Form
from AppGraphic.MojangLogin import Ui_Form as ml
import AppComponement.Mojang as Mojang
import AppComponement.Crack as cracki
import AppComponement.play  as play
#import AppComponement.checkBox as checkBox

os.environ['QT_API'] = 'pyqt5'
CLIENT_ID = ""
SECRET = ""
REDIRECT_URL = ""



class MainWindow(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.saidbis = None
        # setting window icon
        self.setWindowIcon(QIcon("../img/bg1.png"))
        # setting icon text
        self.setWindowIconText("logo")
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        videoWidget = QVideoWidget()
        self.ui.setupUi(self)
        self.ui.download.hide()
        self.ui.play.setProperty('class', 'warning')
        self.ui.comboBox_3.addItem("vanilla")
        self.ui.comboBox_3.addItem("Forge")
        self.w = None
        self.ui.openFolder.clicked.connect(self.openFolder)
        self.ui.accounte.clicked.connect(self.Window2)
        self.ui.play.clicked.connect(self.play)
        #self.ui.play.clicked.connect(self.)
        self.ui.comboBox_2.addItem("Alpha67-server")
        self.minecraft_directory = minecraft_launcher_lib.utils.get_minecraft_directory()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../img/connect logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ui.accounte.setIcon(icon)
        self.ui.accounte.setIconSize(QtCore.QSize(121, 101))

        def sta():
            self.Window2()

        self.ui.label.setPixmap(QtGui.QPixmap("../img/Alpha67 Laucher.png"))
        self.hello()
        self.mediaPlayer.setVideoOutput(videoWidget)
        minecraft_directory = minecraft_launcher_lib.utils.get_minecraft_directory()
        versions = minecraft_launcher_lib.utils.get_version_list()

        for i in versions:
            # Only add release versions
            if i["type"] == "release":
                if not "fo" in i["id"]:
                    self.ui.comboBox_2.addItem(i["id"])

                #self.version_select.addItem(i["id"])

        self.show()

    def openFolder(self):
        print("open alpha folder")
        os.system('cmd /c "start C:/Users\%username%\AppData\Roaming\.alpha67\minecraft"')

    def execute_command(self, command):
        # QProcess.start takes as first argument the program and as second the list of arguments
        # So we need the filter the program from the command
        arguments = command[1:]
        # Deactivate the launch button
        #self.launch_button.setEnabled(False)
        # Clear the text  field
        #self.setPlainText("")
        self.process = QProcess(self)
        # Activate the launch button when Minecraft is closed
        #self.process.finished.connect(lambda: self.play.setEnabled(True))
        # Connect the function to display the output
        #self.process.readyRead.connect(self.dataReady)
        # Start Minecraft
        self.process.start("java", arguments)


    def hello(self):
        th1 = threading.Thread(target=self.smart)
        th1.start()
        th2 = threading.Thread(target=self.updateApp)
        th2.start()
        print("sa")

    def smart(self):
        print("ok")
        time.sleep(15)

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


#start thread
###########################################################
    def mojangThread(self):
        self.Form.close()
        th3 = threading.Thread(target=self.Mojang)
        th3.start()

    def microsoftThread(self):
        self.Form.close()
        th4 = threading.Thread(target=self.microsoft)
        th4.start()

    def crackThread(self):
        self.Form.close()
        th4 = threading.Thread(target=self.Crack)
        th4.start()

    def checkBoxThread(self):
        th5 = threading.Thread(target=self.checkBox)
        th5.start()

    def playThread(self):
        th6 = threading.Thread(target=self.play)
        th6.start()

    def minecraftThread(self):
        th7 = threading.Thread(target=self.minecraft)
        th7.start()
        #self.minecraft()


#thread fonction
###########################################################
    def Mojang(self):
        self.Form.close()
        Mojang.__init__()

    def Crack(self):
        self.Form.close()
        cracki.__init__()

    def microsoft(self):
        self.Form.close()
        os.startfile("microsoftLogin.exe")


    #start the minecraft
    def minecraft(self):

        user = os.getlogin()

        def maximum(max_value, value):
            max_value[0] = value

        version = self.ui.comboBox_2.currentText()

        if version == "Alpha67-server":
            directory = 'C:/Users/'+user+'\AppData\Roaming\.alpha67/alpha/'
            print('start alpha laucher to connect to the server')
            user = os.getlogin()
            motor = "Forge"
            version = "1.16.5"

            def maximum(max_value, value):
                max_value[0] = value

            print('start minecraft')
            max_value = [0]

            def updateBar(value, maxValue):
                percent = 100 * int(value) / int(maxValue[0])
                # print(int(percent))
                self.ui.download.setValue(percent)

            callback = {
                "setStatus": lambda text: print(text),
                "setProgress": lambda value: updateBar(value, max_value),
                "setMax": lambda value: maximum(max_value, value)
            }

            self.ui.download.show()
            self.ui.play.hide()
            print(motor)
            forge_version = minecraft_launcher_lib.forge.find_forge_version(version)
            print(forge_version)

            try:
                forgeLauch = forge_version.replace("-", "-forge-")
            except:
                print("forge version can be download or not exist")
                forgeLauch = None
            print(forgeLauch)

            # if you lauche minecraft vanilla
            if motor == "vanilla":
                minecraft_launcher_lib.install.install_minecraft_version(version, directory, callback=callback)

            # if you lauche ;inecrqft forge
            if motor == "Forge":
                if forge_version == "None":
                    print("version non disponible de forge")

                else:
                    def checkVersionDoawnload():
                        try:
                            directory_mod = 'C:/Users/'+user+'/AppData/Roaming\.alpha67/alpha/versions'
                            files = os.listdir(directory_mod)
                            for f in files:
                                print("file: " + f)
                                if forgeLauch == f:
                                    print("version already download lauching minecraft")
                                    return True
                                    break
                        except:
                            None

                    if checkVersionDoawnload() == None:
                        try:
                            print("doawnloading:" + forgeLauch)
                            minecraft_launcher_lib.forge.install_forge_version(forge_version, directory,
                                                                               callback=callback)
                            print(forgeLauch)

                        except:
                            None

            self.ui.play.show()
            self.ui.download.hide()

            login = self.getSelectVersion()
            print(login)

            ###########
            if login == "mojang":
                print("okok")
                with open('C:/Users/' + user + '\AppData\Roaming\.alpha67/alpha/cred.json', 'r') as file:
                    uInfo = json.load(file)
                    print(uInfo)
                    # uInfo = literal_eval(uInfo)

                    uInfo = uInfo['mojang']
                    uInfo = uInfo[0]
                    username = uInfo['username']
                    password = uInfo['password']

                passwordEnc = str(user + "67")
                password = password.replace("'", '')
                password = password[1:]
                print(password)
                username = username.replace("'", '')
                username = username[1:]
                print(username)
                pa = encrypte.password_decrypt(password, passwordEnc).decode()
                us = encrypte.password_decrypt(username, passwordEnc).decode()

                login_data = minecraft_launcher_lib.account.login_user(us, pa)
                print(login_data)
                options = {
                    "username": login_data["selectedProfile"]["name"],
                    "uuid": login_data["selectedProfile"]["id"],
                    "token": login_data["accessToken"]
                }

                if motor == "vanilla":
                    command = minecraft_launcher_lib.command.get_minecraft_command(version, minecraft_directory,
                                                                                   options)
                    self.execute_command(command)
                elif motor == "Forge":
                    print("crack, lauching minecraft, version:" + forgeLauch)
                    directory = 'C:/Users/'+user+'\AppData\Roaming\.alpha67/alpha/'
                    minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(
                        forgeLauch, directory, options)

                    subprocess.call(minecraft_command)

            #################################################################################################
            if login == "microsoft":
                print("okok")
                with open('C:/Users/' + user + '\AppData\Roaming\.alpha67/alpha/ACI.json', 'r') as file:
                    uInfo = json.load(file)
                    print(uInfo)
                    # uInfo = literal_eval(uInfo)
                options = {
                    "username": uInfo["name"],
                    "uuid": uInfo["id"],
                    "token": uInfo["access_token"]
                }

                if motor == "vanilla":
                    command = minecraft_launcher_lib.command.get_minecraft_command(version, minecraft_directory,
                                                                                   options)
                    self.execute_command(command)
                elif motor == "Forge":
                    print("crack, lauching minecraft, version:" + forgeLauch)
                    directory = 'C:/Users/'+user+'\AppData\Roaming\.alpha67/alpha/'
                    minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(
                        forgeLauch, directory, options)

                    subprocess.call(minecraft_command)

            #########################################################################################################
            if login == "crack":
                print("okoksss")
                with open('C:/Users/' + user + '\AppData\Roaming\.alpha67/alpha/cred.json', 'r') as file:
                    uInfo = json.load(file)
                    print(uInfo)
                    uInfo = uInfo['crack']
                    uInfo = uInfo[0]
                    username = uInfo['username']
                    # uInfo = literal_eval(uInfo)
                options = {
                    "username": username,
                    "uuid": uuid.uuid4().hex,
                    "token": ""
                }

                print(forge_version)
                print(motor)
                if motor == "vanilla":
                    command = minecraft_launcher_lib.command.get_minecraft_command(version, minecraft_directory,
                                                                                   options)
                    self.execute_command(command)
                elif motor == "Forge":
                    try:
                        print("crack, lauching minecraft, version:" + forgeLauch)
                        directory = 'C:/Users/'+user+'\AppData\Roaming\.alpha67/alpha/'
                        minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(
                            forgeLauch, directory, options)
                        print(minecraft_command)

                        subprocess.call(minecraft_command)
                    except:
                        None

        else:
            motor = self.ui.comboBox_3.currentText()
            version = self.ui.comboBox_2.currentText()
            user = os.getlogin()
            def maximum(max_value, value):
                max_value[0] = value

            print('start minecraft')
            max_value = [0]

            def updateBar(value, maxValue):
                percent = 100 * int(value) / int(maxValue[0])
                #print(int(percent))
                self.ui.download.setValue(percent)

            callback = {
                "setStatus": lambda text: print(text),
                "setProgress": lambda value: updateBar(value, max_value),
                "setMax": lambda value: maximum(max_value, value)
            }


            self.ui.download.show()
            self.ui.play.hide()
            print(motor)
            forge_version = minecraft_launcher_lib.forge.find_forge_version(version)
            print(forge_version)

            try:
                forgeLauch = forge_version.replace("-", "-forge-")
            except:
                print("forge version can be download or not exist")
                forgeLauch = None
            print(forgeLauch)

            #if you lauche minecraft vanilla
            if motor == "vanilla":
                minecraft_launcher_lib.install.install_minecraft_version(version, directory, callback=callback)

            #if you lauche ;inecrqft forge
            if motor == "Forge":
                if forge_version == "None":
                    print("version non disponible de forge")

                else:
                    def checkVersionDoawnload():
                        directory_mod = 'C:/Users/'+user+'\AppData\Roaming\.alpha67\minecraft/versions'
                        files = os.listdir(directory_mod)
                        for f in files:
                            print("file: "+f)
                            if forgeLauch == f:
                                print("version already download lauching minecraft")
                                return True
                                break

                    if checkVersionDoawnload() == None:
                        try:
                            print("doawnloading:"+forgeLauch)
                            minecraft_launcher_lib.forge.install_forge_version(forge_version, directory,
                                                                               callback=callback)
                            print(forgeLauch)

                        except:
                            None

            self.ui.play.show()
            self.ui.download.hide()

            login = self.getSelectVersion()
            print(login)


            ###########
            if login == "mojang":
                print("okok")
                with open('C:/Users/' + user + '\AppData\Roaming\.alpha67/alpha/cred.json', 'r') as file:
                    uInfo = json.load(file)
                    print(uInfo)
                    # uInfo = literal_eval(uInfo)

                    uInfo = uInfo['mojang']
                    uInfo = uInfo[0]
                    username = uInfo['username']
                    password = uInfo['password']

                passwordEnc = str(user + "67")
                password = password.replace("'", '')
                password = password[1:]
                print(password)
                username = username.replace("'", '')
                username = username[1:]
                print(username)
                pa = encrypte.password_decrypt(password, passwordEnc).decode()
                us = encrypte.password_decrypt(username, passwordEnc).decode()

                login_data = minecraft_launcher_lib.account.login_user(us, pa)
                print(login_data)
                options = {
                    "username": login_data["selectedProfile"]["name"],
                    "uuid": login_data["selectedProfile"]["id"],
                    "token": login_data["accessToken"]
                }


                if motor == "vanilla":
                    command = minecraft_launcher_lib.command.get_minecraft_command(version, minecraft_directory,
                                                                                   options)
                    self.execute_command(command)
                elif motor == "Forge":
                    print("crack, lauching minecraft, version:"+forgeLauch)
                    directory = 'C:/Users/'+user+'\AppData\Roaming\.alpha67/alpha/'
                    minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(
                        forgeLauch, directory, options)

                    subprocess.call(minecraft_command)


            #################################################################################################
            if login == "microsoft":
                print("okok")
                with open('C:/Users/' + user + '\AppData\Roaming\.alpha67/alpha/ACI.json', 'r') as file:
                    uInfo = json.load(file)
                    print(uInfo)
                    # uInfo = literal_eval(uInfo)
                options = {
                    "username": uInfo["name"],
                    "uuid": uInfo["id"],
                    "token": uInfo["access_token"]
                }

                if motor == "vanilla":
                    command = minecraft_launcher_lib.command.get_minecraft_command(version, minecraft_directory,
                                                                                   options)
                    self.execute_command(command)
                elif motor == "Forge":
                    print("crack, lauching minecraft, version:"+forgeLauch)
                    directory = 'C:/Users/'+user+'\AppData\Roaming\.alpha67/alpha/'
                    minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(
                        forgeLauch, directory, options)

                    subprocess.call(minecraft_command)

            #########################################################################################################
            if login == "crack":
                print("okoksss")
                with open('C:/Users/' + user + '\AppData\Roaming\.alpha67/alpha/cred.json', 'r') as file:
                    uInfo = json.load(file)
                    print(uInfo)
                    uInfo = uInfo['crack']
                    uInfo = uInfo[0]
                    username = uInfo['username']
                    # uInfo = literal_eval(uInfo)
                options = {
                    "username": username,
                    "uuid": uuid.uuid4().hex,
                    "token": ""
                }

                print(forge_version)
                print(motor)
                if motor == "vanilla":
                    command = minecraft_launcher_lib.command.get_minecraft_command(version, minecraft_directory,
                                                                                   options)
                    self.execute_command(command)
                elif motor == "Forge":
                    try:
                        print("crack, lauching minecraft, version:"+forgeLauch)
                        directory = 'C:/Users/'+user+'\AppData\Roaming\.alpha67/alpha/'
                        minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(
                            forgeLauch, directory, options)
                        print(minecraft_command)

                        subprocess.call(minecraft_command)
                    except:
                        None


    def play(self):

        user = os.getlogin()

        def showDialog():
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText("Vous devez vous connecter afin de lancer le jeu !!")
            msgBox.setWindowTitle("Attention")
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

            returnValue = msgBox.exec()
            if returnValue == QMessageBox.Ok:
                self.Window2()


        def checkLogin():

            try:
                with open("C:/Users/" + user + "\AppData\Roaming\.alpha67/alpha/select.json", "r") as jsonFile:
                    data = json.load(jsonFile)
                    crack = data["crack"][0]["connect"]
                    microsoft = data["microsoft"][0]["connect"]
                    mojang = data["mojang"][0]["connect"]

                if crack == "True":
                    return True
                elif microsoft == "True":
                    return True
                elif mojang == "True":
                    return True
                else:
                    print("please connects")
                    showDialog()
                    return False

            except:
                print("please connect")
                showDialog()

        if checkLogin() == True:
            self.minecraftThread()


    def getSelectVersion(self):
        user = os.getlogin()
        try:
            with open("C:/Users/" + user + "\AppData\Roaming\.alpha67/alpha/select.json", "r") as jsonFile:
                data = json.load(jsonFile)
                crack = data["crack"][0]["select"]
                microsoft = data["microsoft"][0]["select"]
                mojang = data["mojang"][0]["select"]

            if crack == "True":
                return "crack"
            elif microsoft == "True":
                return "microsoft"
            elif mojang == "True":
                return "mojang"
            else:
                print("please connects")

        except:
            print("please connect")









    def Window2(self):
        user = os.getlogin()
        self.Form = QtWidgets.QWidget()
        self.uiw = Ui_Form()
        self.uiw.setupUi(self.Form)
        self.Form.show()

        x = {

                "mojang": [
                    {"connect": "False", "select": "False"}
                ],
                "microsoft": [
                    {"connect": "False", "select": "False"}
                ],
                "crack": [
                    {"connect": "False", "select": "False"}
                ]
            }

        if os.path.isfile("C:/Users/" + user + "\AppData\Roaming\.alpha67/alpha/select.json") == True:
            with open("C:/Users/" + user + "\AppData\Roaming\.alpha67/alpha/select.json", "r") as jsonFile:
                data = json.load(jsonFile)
            if data["mojang"][0]["select"] == "True":
                self.uiw.checkBox.setChecked(True)
            if data["microsoft"][0]["select"] == "True":
                self.uiw.checkBox_2.setChecked(True)
            if data["crack"][0]["select"] == "True":
                self.uiw.checkBox_3.setChecked(True)

        else:
            with open("C:/Users/" + user + "\AppData\Roaming\.alpha67/alpha/select.json", "w") as jsonFile:
                json.dump(x,jsonFile)

        def checkBox():
            if self.uiw.checkBox.isChecked() == True:
                self.uiw.checkBox_3.setChecked(False)
                self.uiw.checkBox_2.setChecked(False)
                with open("C:/Users/" + user + "\AppData\Roaming\.alpha67/alpha/select.json", "r") as jsonFile:
                    data = json.load(jsonFile)
                    print(type(data))
                    print(data["mojang"][0]["connect"])
                if data["mojang"][0]["connect"] == "False":
                    self.Mojang()

                with open("C:/Users/" + user + "\AppData\Roaming\.alpha67/alpha/select.json", "r") as jsonFile:
                    data = json.load(jsonFile)
                    print(data)

                data["mojang"][0]["select"] = "True"
                data["microsoft"][0]["select"] = "False"
                data["crack"][0]["select"] = "False"
                print(data)
                with open("C:/Users/" + user + "\AppData\Roaming\.alpha67/alpha/select.json", "w") as jsonFile:
                    json.dump(data, jsonFile)

        def checkBox3():
            if self.uiw.checkBox_3.isChecked() == True:
                self.uiw.checkBox.setChecked(False)
                self.uiw.checkBox_2.setChecked(False)
                with open("C:/Users/" + user + "\AppData\Roaming\.alpha67/alpha/select.json", "r") as jsonFile:
                    data = json.load(jsonFile)
                    print(type(data))
                    print(data["crack"][0]["connect"])
                if data["crack"][0]["connect"] == "False":
                    self.Crack()
                with open("C:/Users/" + user + "\AppData\Roaming\.alpha67/alpha/select.json", "r") as jsonFile:
                    data = json.load(jsonFile)
                    print(data)

                data["mojang"][0]["select"] = "False"
                data["microsoft"][0]["select"] = "False"
                data["crack"][0]["select"] = "True"
                print(data)
                with open("C:/Users/" + user + "\AppData\Roaming\.alpha67/alpha/select.json", "w") as jsonFile:
                    json.dump(data, jsonFile)
        def checkBox2():
            if self.uiw.checkBox_2.isChecked() == True:
                self.uiw.checkBox.setChecked(False)
                self.uiw.checkBox_3.setChecked(False)
                with open("C:/Users/" + user + "\AppData\Roaming\.alpha67/alpha/select.json", "r") as jsonFile:
                    data = json.load(jsonFile)
                    print(type(data))
                    print(data["microsoft"][0]["connect"])
                if data["microsoft"][0]["connect"] == "False":
                    self.microsoft()
                with open("C:/Users/" + user + "\AppData\Roaming\.alpha67/alpha/select.json", "r") as jsonFile:
                    data = json.load(jsonFile)
                    print(data)

                data["mojang"][0]["select"] = "False"
                data["microsoft"][0]["select"] = "True"
                data["crack"][0]["select"] = "False"
                print(data)
                with open("C:/Users/" + user + "\AppData\Roaming\.alpha67/alpha/select.json", "w") as jsonFile:
                    json.dump(data, jsonFile)
        self.uiw.mojang.clicked.connect(self.Mojang)
        self.uiw.microsoft.clicked.connect(self.microsoft)
        self.uiw.crack.clicked.connect(self.Crack)
        self.uiw.checkBox.stateChanged.connect(checkBox)
        self.uiw.checkBox_2.stateChanged.connect(checkBox2)
        self.uiw.checkBox_3.stateChanged.connect(checkBox3)










if __name__ == "__main__":
    extra = {

        # Button colors
        'danger': '#dc3545',
        'warning': '#ffc107',
        'success': '#17a2b8',

        # Font
        'font-family': 'Roboto',
    }

    app = QApplication(sys.argv)
    #apply_stylesheet(app, theme='dark_teal.xml', invert_secondary=True, extra=extra)

    stylesheet = app.styleSheet()
    window = MainWindow()
    sys.exit(app.exec_())
