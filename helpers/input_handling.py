from helpers.constants import *

def validate_input(prompt, expected_type, error_message):
    while True:
        user_input = input(L_YELLOW + prompt + RESET)
        try:
            user_input = expected_type(user_input)
            return user_input
        except ValueError:
            print(L_RED + error_message + RESET)

# Asks users for their password
def password_check(PASSWORD_D):

    """
    Asks the user for password and checks if it is correct
    
    Args:
        PASSWORD_D (str): password
    
    Returns:
        bool: validity of password
    """
    
    while True:
        user_input = input(L_YELLOW + "Enter password: " + RESET)
        if user_input == PASSWORD_D:
            return True
        else:
            print(L_RED + "Incorrect password. Please try again." + RESET)