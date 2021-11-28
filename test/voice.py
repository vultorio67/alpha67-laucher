#!/usr/bin/env python3
# This example shows how to write a basic launcher with Tkinter.
from tkinter import Tk, Label, Entry, Button, mainloop
from tkinter.ttk import Combobox
import minecraft_launcher_lib
import subprocess
import sys



login_data = minecraft_launcher_lib.account.login_user("evan_marion15@outlook.fr", "#Evan152005")
print(login_data)

options = {
    "username": login_data["selectedProfile"]["name"],
    "uuid": login_data["selectedProfile"]["id"],
    "token": login_data["accessToken"]
}
directory = 'C:/Users\evanm\AppData\Roaming\.alpha67\minecraft/'
minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(
    "1.15.2-forge-31.0.0", directory, options)

subprocess.call(minecraft_command)
