# Imports packages
from cryptography.fernet import Fernet
import base64
from helpers.constants import L_CYAN, L_RED, L_YELLOW, L_GREEN, RESET, DEFAULT_E
from helpers.environment import setupEnvironment, updateEnvironment
from helpers.input_handling import validate_input
from helpers.key_management import generate_key, outputKey, manageKeys
from helpers.cryptography import encrypt_func, decrypt_func, encryptFile, decryptFile

# Loads the environment
setupEnvironment()

# Main Menu
def main():
    """
    Prints out the welcome screen and asks the user for their choice

    Args:
        None

    Returns:
        int: users menu choice
    """
    menu_options = [
        L_CYAN + "1. Encrypt",
        L_CYAN + "2. Decrypt",
        L_CYAN + "3. Print out your current key",
        L_CYAN + "4. Set password",
        L_CYAN + "5. Reset Password and Key",
        L_CYAN + "6. Manage Keys",
        L_CYAN + "7. Encrypt a file",
        L_CYAN + "8. Decrypt a file",
        L_CYAN + "0. Exit" + RESET
    ]

    print("\n".join(menu_options))

    while True:
        choice = validate_input("Input a number: ", int, "Please input a valid number")
        if 0 <= choice <= 8:
            return choice
        else:
            print(L_RED + "Invalid choice. Please select a number between 0 and 8." + RESET)

# Changes password
def setPassword(PASSWORD_D):

    """
    Changes the password

    Args:
        PASSWORD_D (str): password

    Returns:
        None
    
    """
    
    print(L_RED + "Warning for security reasons this will reset your key as well so you cant access someone elses encryptions by resetting password." + RESET)
    generate_key(PASSWORD_D)

    while True:
        password_d = input(L_YELLOW + "Input new Password: " + RESET)
        double_check = input(L_YELLOW + "Input new Password again: " + RESET)

        if password_d != double_check:
            print(L_RED + "Passwords do not match" + RESET)
        else:
            break

    password_e = base64.b64encode(bytes(password_d, encoding="utf-8"))
    print(L_GREEN + "Password set" + RESET)

    updateEnvironment(KEY=None, KEY_BACKUP=None, PASSWORD_E=password_e.decode("utf-8", "strict"))

# Resets the password and generates a new key
def reset(PASSWORD_D):

    """
    Resets the password and generates a new key

    Args:
        PASSWORD_D (str): password

    Returns:
        None
    
    """

    generate_key(PASSWORD_D)
    
    updateEnvironment(KEY=None, KEY_BACKUP=None, PASSWORD_E=DEFAULT_E)

    print(L_GREEN + "Password and key reset" + RESET)        

# Prompts user if they would like to end the script 
def end():

    """
    Prompts user if they would like to end the script

    Args:
        None
    
    Returns:
        None
    
    """

    while True:
            end = input(L_YELLOW + "End [y/n]" + RESET)

            try:
                end = str(end)
            except ValueError:
                print(L_RED + "Please input y or n" + RESET)
                continue

            if end.lower() in ["yes", "y", "no", "n"]:
                if end.lower() in ["yes", "y"]:
                    exit()
                elif end.lower() in ["no", "n"]:
                    return
            else:
                print(L_RED + "Please input y or n" + RESET)

if __name__ == "__main__":

    KEY, KEY_BACKUP, PASSWORD_E, PASSWORD_D, = setupEnvironment()

    if KEY == "" or KEY == None or PASSWORD_D == "alpine" or PASSWORD_D == None or PASSWORD_D == "":
        print(L_CYAN + "Either this is your first time running the script or YOU changed you key to '',no worries we are generating a new key for you." + RESET)
        print(L_CYAN + "Default password is 'alpine' you will be prompted to change it after the key is generated." + RESET)
        generate_key(PASSWORD_D)
        print(L_CYAN + "Please change your password" + RESET)
        setPassword(PASSWORD_D)
        
else:

    print(L_RED + "This script is not meant to be run as a module. Please run it as a standalone script." + RESET)

# Controls the users choice throughout the script      
while True:

    KEY, KEY_BACKUP, PASSWORD_E, PASSWORD_D = setupEnvironment()

    choice = main()
    
    # I use match statements because they are easier to read and more efficient than if statements
    match choice:                                   

        case 1:
            encrypt = encrypt_func(KEY)
            print(L_GREEN + encrypt + RESET)
        case 2:
            decrypt = decrypt_func(KEY, PASSWORD_D)
            print(L_GREEN + decrypt + RESET)
        case 3:
            outputKey(KEY, PASSWORD_D)
        case 4:
            setPassword(PASSWORD_D)
        case 5:
            reset(PASSWORD_D)
        case 6:
            manageKeys(KEY, KEY_BACKUP)
        case 7:
            encryptFile(KEY)
        case 8:
            decryptFile(KEY, PASSWORD_D)
        case 0:
            print(L_CYAN + "The script will now stop" + RESET)
            exit()

    end()