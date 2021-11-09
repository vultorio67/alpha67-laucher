import secrets
from base64 import urlsafe_b64encode as b64e, urlsafe_b64decode as b64d

from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

from minecraft_launcher_lib import *
import minecraft_launcher_lib
import os
import json
from ast import literal_eval

user = os.getlogin()

if minecraft_launcher_lib.microsoft_account.url_contains_auth_code(url.toString()):
    # Get the code from the url
    auth_code = minecraft_launcher_lib.microsoft_account.get_auth_code_from_url(url.toString())
    # Do the login
    account_informaton = minecraft_launcher_lib.microsoft_account.complete_login(CLIENT_ID, SECRET, REDIRECT_URL,
                                                                                 auth_code)
    # Show the login information
    show_account_information(account_informaton)
