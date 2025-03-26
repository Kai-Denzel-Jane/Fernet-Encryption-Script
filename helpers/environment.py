import os
import base64
from dotenv import load_dotenv, set_key
from helpers.constants import *

def setupEnvironment():

    if not load_dotenv(dotenv_path=".env"):
        print(L_RED + "No .env file found, creating one for you." + RESET)
        with open(".env", "w") as file:
            file.close()

        load_dotenv(dotenv_path=".env")
        set_key(".env", "PASSWORD", DEFAULT_E)
        set_key(".env", "PASSWORD", DEFAULT_E)
        set_key(".env", "KEY_BACKUP", "")
        set_key(".env", "KEY", "")

    os.environ.clear()
    load_dotenv(dotenv_path=".env")
    KEY = os.getenv("KEY")
    KEY_BACKUP = os.getenv("KEY_BACKUP")
    PASSWORD_E = os.getenv("PASSWORD")
    PASSWORD_D = base64.b64decode(PASSWORD_E).decode("utf-8", "strict")
    if PASSWORD_E:
        PASSWORD_D = base64.b64decode(PASSWORD_E).decode("utf-8", "strict")

    print(L_CYAN + "Environment variables loaded successfully." + RESET)
    return KEY, KEY_BACKUP, PASSWORD_E, PASSWORD_D


def updateEnvironment(KEY, KEY_BACKUP, PASSWORD_E):

    load_dotenv(dotenv_path=".env")

    if KEY is not None:
        set_key(".env", "KEY", KEY)
    if KEY_BACKUP is not None:
        set_key(".env", "KEY_BACKUP", KEY_BACKUP)
    if PASSWORD_E is not None:
        set_key(".env", "PASSWORD", PASSWORD_E)

    os.environ.clear()
    load_dotenv(dotenv_path=".env")

    print(L_GREEN + "Environment variables updated successfully." + RESET)

def loadEnvironment():

    os.environ.clear()
    load_dotenv(dotenv_path=".env")
    KEY = os.getenv("KEY")
    KEY_BACKUP = os.getenv("KEY_BACKUP")
    PASSWORD_E = os.getenv("PASSWORD")
    PASSWORD_D = base64.b64decode(PASSWORD_E).decode("utf-8", "strict")

    return KEY, KEY_BACKUP, PASSWORD_E, PASSWORD_D