from cryptography.fernet import Fernet
import cryptography.fernet
from helpers.constants import *
from helpers.input_handling import *
import os

# Encryption and Decryption functions

# Encrypt function
def encrypt_func(KEY):

    """
    Encrypts the text the user inputs

    Args:
        KEY (str): encryption key

    Returns:
        str: encrypted text

    """
    text = input(L_YELLOW + "Input text: " + RESET)

    # if text == EXIT_CODE:
    #     return

    data = bytes(text, encoding="utf-8")
    try:
        fernet_cipher = Fernet(KEY)
        encrypted_text = fernet_cipher.encrypt(data)
    except (ValueError, TypeError) as e:
        print(L_RED + "Invalid encryption key." + RESET)
        return None

    return(str(encrypted_text))

# Decrypt function
def decrypt_func(KEY, PASSWORD_D):
    """
    Decrypts the text the user inputs

    Args:
        KEY (str): encryption key
        PASSWORD_D (str): password

    Returns:
        str: decrypted text
    """

    if password_check(PASSWORD_D) == True:

        data = input(L_YELLOW + "Input text: " + RESET)

        # Remove the "b'" and "'" from the input if they exist
        if data.startswith("b'") and data.endswith("'"):
            data = data[2:-1]

        # Try to decrypt the data
        try:
            encryption_tool = Fernet(KEY)
            decrypted_text = encryption_tool.decrypt(data.encode())
        except cryptography.fernet.InvalidToken as e:
            print(L_RED + "Invalid token.", str(e) + RESET)
            decrypted_text = "YOUR KEY IS INVALID"
            return decrypted_text
        except:
            print(L_RED + "Decryption failed." + RESET)
            decrypted_text = "DECRYPTION FAILED"
            return decrypted_text

        # Try to decode the decrypted data
        try:
            decrypted_text = decrypted_text.decode("utf-8", "strict")
        except Exception as e:
            print(L_RED + "Decoding failed.", str(e) + RESET)
            return

        return decrypted_text
    else:
        password_check(PASSWORD_D)

def encryptFile(KEY):

    """
    Encrypts a file

    Args:
        KEY (str): encryption key
    
    Returns:
        None
    
    """

    
    cwd_contents = os.listdir(os.curdir)

    for item in cwd_contents:
        print(L_CYAN + item + RESET)

    filename = input(L_YELLOW + "Input file name: " + RESET)
    
    with open(filename, "rb") as file:

        data = file.read()

    encryption_tool = Fernet(KEY)
    encrypted = encryption_tool.encrypt(data)

    with open(filename, "wb") as file:

        file.write(encrypted)
        print(L_GREEN + "File encrypted" + RESET)


def decryptFile(KEY, PASSWORD_D):
    
    """
    Decrypts a file

    Args:
        KEY (str): encryption key
        PASSWORD_D (str): password
    
    Returns:
        None
    
    """

    if password_check(PASSWORD_D) == True:
        cwd_contents = os.listdir(os.curdir)

        for item in cwd_contents:
            print(L_CYAN + item + RESET)

        filename = input(L_YELLOW + "Input file name: " + RESET)
    
        with open(filename, "rb") as file:

            data = file.read()

        encryption_tool = Fernet(KEY)
        decrypted = encryption_tool.decrypt(data)

        with open(filename, "wb") as file:

            file.write(decrypted)
            print(L_GREEN + "File decrypted" + RESET)

    else:
        password_check(PASSWORD_D)