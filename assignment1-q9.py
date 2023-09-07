import re

def is_valid_password(password):
    # Check if the password length is at least five characters
    if len(password) < 5:
        return False

    # Check if the password contains the symbol "&"
    if '&' not in password:
        return False

    # Check if the password contains at least one uppercase letter
    if not any(char.isupper() for char in password):
        return False

    # Check if the password contains at least one lowercase letter
    if not any(char.islower() for char in password):
        return False

    # If all checks pass, the password is valid
    return True

# Prompt the user to enter a password
password = input("Enter a password: ")

# Check if the entered password is valid
if is_valid_password(password):
    print("Password is valid.")
else:
    print("Password does not meet the requirements.")