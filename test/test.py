from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtCore import QUrl, QLocale
import minecraft_launcher_lib
import json
import sys
import os

CLIENT_ID = "f2107422-b90b-46cf-9d04-3dd3da989b44"
SECRET = "483ec922-7c9a-4d16-9281-0d42e802a802"
REDIRECT_URL = "https://github.com/vultorio67/alpha67-downloader"


class LoginWindow(QWebEngineView):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login Window Example")

        # Set the path where the refresh token is saved
        self.refresh_token_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "refresh_token.json")
        print(self.refresh_token_file)

        # Login with refresh token, if it exists
        if os.path.isfile(self.refresh_token_file):
            print("ok")
            with open(self.refresh_token_file, "r", encoding="utf-8") as f:
                refresh_token = json.load(f)
                # Do the login with refresh token
                try:
                    account_informaton = minecraft_launcher_lib.microsoft_account.complete_refresh(CLIENT_ID, SECRET, REDIRECT_URL, refresh_token)
                    self.show_account_information(account_informaton)
                    return
                # Show the window if the refresh token is invalid
                except minecraft_launcher_lib.exceptions.InvalidRefreshToken:
                    pass

        # Open the login url
        print("ok2")
        self.load(QUrl(minecraft_launcher_lib.microsoft_account.get_login_url(CLIENT_ID, REDIRECT_URL)))
        print("ok3")
        # Connects a function that is called when the url changed
        self.urlChanged.connect(self.new_url)
        print("ok4")
        self.show()

    def new_url(self, url: QUrl):

        print("ok5")
        # Check if the url contains the code
        if minecraft_launcher_lib.microsoft_account.url_contains_auth_code(url.toString()):
            # Get the code from the url
            auth_code = minecraft_launcher_lib.microsoft_account.get_auth_code_from_url(url.toString())
            # Do the login
            #account_informaton = minecraft_launcher_lib.microsoft_account.complete_login(CLIENT_ID, SECRET, REDIRECT_URL, auth_code)
            # Show the login information
            #self.show_account_information(account_informaton)

    def show_account_information(self, information_dict):
        information_string = f'Username: {information_dict["name"]}<br>'
        information_string += f'UUID: {information_dict["id"]}<br>'
        information_string += f'Token: {information_dict["access_token"]}<br>'

        # Save the refresh token in a file
        with open(self.refresh_token_file, "w", encoding="utf-8") as f:
            json.dump(information_dict["refresh_token"], f, ensure_ascii=False, indent=4)

        message_box = QMessageBox()
        message_box.setWindowTitle("Account information")
        message_box.setText(information_string)
        message_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        message_box.exec()

        # Exit the program
        sys.exit(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # This line sets the language of the webpage to the system language
    QWebEngineProfile.defaultProfile().setHttpAcceptLanguage(QLocale.system().name().split("_")[0])
    w = LoginWindow()
    sys.exit(app.exec())
