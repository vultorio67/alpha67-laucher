from tkinter import Tk, Label, Entry, Button, mainloop
from tkinter.ttk import Combobox
import minecraft_launcher_lib
import subprocess
import sys
import uuid

forge_version = minecraft_launcher_lib.forge.find_forge_version("1.16.5")
print(forge_version)

mc_ver = "1.16.5"

test = mc_ver[:7]+"forge-"+mc_ver[7:]
print(test)


def main():
    def launch():
        window.withdraw()

        minecraft_launcher_lib.install.install_minecraft_version(version_select.get(), minecraft_directory)

        login_data = minecraft_launcher_lib.account.login_user(username_input.get(), password_input.get())

        options = {
            "username": "Lapetitecuillere",
            "uuid": "d95575fa0cb5486c8b430e0a807ee41",
            "token": "eyJhbGciOiJIUzI1NiJ9.eyJ4dWlkIjoiMjUzNTQyMTI1MTI4ODc5MiIsImFnZyI6IkFkdWx0Iiwic3ViIjoiMTk5OWJkZjQtYTBkMy00YTlkLTkzNWQtNjc2MTE1NTNiMDU1IiwibmJmIjoxNjM2NjMxNTQ0LCJhdXRoIjoiWEJPWCIsInJvbGVzIjpbXSwiaXNzIjoiYXV0aGVudGljYXRpb24iLCJleHAiOjE2MzY3MTc5NDQsImlhdCI6MTYzNjYzMTU0NCwicGxhdGZvcm0iOiJVTktOT1dOIiwieXVpZCI6ImJiNGZlZTgwNjMxNWUxMTM3ZTUxNmU0NjU2YmQyMmE0In0.6llfDoc5TXYvyXUDGUjieeBzjCkzLsH0Ym74MiYi0Go"
        }

        minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(version_select.get(), minecraft_directory, options)

        si = subprocess.STARTUPINFO()
        si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        subprocess.call(minecraft_command, startupinfo=si)

        sys.exit(0)

    window = Tk()
    window.title("Minecraft Launcher")

    Label(window, text="Username:").grid(row=0, column=0)
    username_input = Entry(window)
    username_input.grid(row=0, column=1)
    Label(window, text="Password:").grid(row=1, column=0)
    password_input = Entry(window)
    password_input.grid(row=1, column=1)

    minecraft_directory = minecraft_launcher_lib.utils.get_minecraft_directory()
    versions = minecraft_launcher_lib.utils.get_available_versions(minecraft_directory)
    version_list = []

    for i in versions:
        version_list.append(i["id"])

    Label(window, text="Version:").grid(row=2, column=0)
    version_select = Combobox(window, values=version_list)
    version_select.grid(row=2, column=1)
    version_select.current(0)

    Button(window, text="Launch", command=launch).grid(row=4, column=1)

    mainloop()


if __name__ == "__main__":
    main()
