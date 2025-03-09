from helpers.constants import *
from helpers.environment import *
from helpers.input_handling import *
from cryptography.fernet import Fernet

KEY, KEY_BACKUP, PASSWORD_E, PASSWORD_D  = loadEnvironment()

# Key generation
def generate_key(PASSWORD_D):

    """
    Generates a new key and saves it to .env file

    Args:
        PASSWORD_D (str): password
    
    Returns:
        None
    
    """

    if password_check(PASSWORD_D) == True:

        key = Fernet.generate_key()
        key_str = key.decode("utf-8", "strict")

        updateEnvironment(KEY=key_str, KEY_BACKUP=None, PASSWORD_E=None)
        print(L_GREEN + "Key generated" + RESET)

    else:
        password_check(PASSWORD_D)

# Import custom keys so you can share encrypted messages with others
def custom_key(PASSWORD_D):

    """
    Imports a custom key and saves it to .env file

    Args:
        PASSWORD_D (str): password

    Returns:
        None
    
    """

    if password_check(PASSWORD_D) == True:

        key = input(L_YELLOW + "Input key: " + RESET)
        key = bytes(key, encoding="utf-8")
        key_str = key.decode("utf-8", "strict")
        updateEnvironment(KEY=key_str, KEY_BACKUP=None, PASSWORD_E=None)
    else:

        password_check(PASSWORD_D)

def outputKey(KEY, PASSWORD_D):

    """
    Prints out the current key

    Args:
        KEY (str): encryption key
        PASSWORD_D (str): password

    Returns:
        None

    """
    
    if password_check(PASSWORD_D) == True:
        print(L_CYAN + KEY + RESET)
    else:
        password_check(PASSWORD_D)

def manageKeys(KEY, KEY_BACKUP):
    """
    Manages keys

    This function allows the user to perform various operations on encryption keys, such as backing up a key, deleting a backed up key, and restoring a backed up key as the current key.

    Args:
        KEY_BACKUP (str): backed up key
    
    Returns:
        None
    """
    while True:
        print(L_CYAN + "1. Generate a new key (backups the previous key)" + RESET)
        print(L_CYAN + "2. Backup a key" + RESET)
        print(L_CYAN + "3. Delete backed up key" + RESET)
        print(L_CYAN + "4. Input a custom key" + RESET)
        print(L_CYAN + "5. Print out key, and backed up key" + RESET)
        print(L_CYAN + "6. Restore backed up key as current key" + RESET)
        print(L_CYAN + "0. Go back to main menu" + RESET)
        option_key = validate_input("Input a number: ", int, "Please input a number")

        match option_key:
            case 1:
                print(L_RED + "Warning this will backup your current key, wiping any previous backups as well." + RESET)
                user_input = input(L_YELLOW + "Are you sure [y/n]" + RESET)
                if user_input == "y":

                    updateEnvironment(KEY=generate_key(PASSWORD_D), KEY_BACKUP=None, PASSWORD_E=None)
                    break
            case 2:
                if KEY_BACKUP != '':
                    print(L_RED + "Delete this backed up key first" + RESET)

                user_input = input(L_YELLOW + "Input the key: " + RESET)
                updateEnvironment(KEY=None, KEY_BACKUP=KEY, PASSWORD_E=None)
                break
            case 3:
                user_input = input(L_YELLOW + "Are you sure [y/n]" + RESET)
                if user_input == "y":
                    updateEnvironment(KEY=None, KEY_BACKUP="", PASSWORD_E=None)
                    break
            case 4:
                custom_key(PASSWORD_D)
                break
            case 5:
                print(L_CYAN + f"Key: {KEY}" + RESET)
                print(L_CYAN + f"Backed up key: {KEY_BACKUP}" + RESET)

            case 6:
                user_input = input(L_YELLOW + "Are you sure [y/n]" + RESET)
                if user_input == "y":
                    updateEnvironment(KEY=KEY_BACKUP, KEY_BACKUP=None, PASSWORD_E=None)
                    break

            case 0:
                break