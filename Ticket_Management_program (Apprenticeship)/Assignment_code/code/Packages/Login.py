import os
import sys

from Assignment_code.code.Packages.clear import clear
from cryptography.fernet import Fernet


def login():
    ext = ".txt"  # the user data is saved in a text document with the same name as the user but so .txt needs to be ammened to the username to open the file
    try:  # checks that the enviroment variables are still assigned
        key_path = os.environ["ENVIRO_KEY_PATH"]
        User_path = os.environ["ENVIRO_USER_PATH"]

    except OSError as e:  # if there is an error then an exception is raised
        print(f"ERROR: {e}")
        sys.exit()

    file = open(key_path)  # fetches the encryption key
    key = file.read()
    clear()
    print("-----------------------------------------")
    print("User Login:")
    print("-----------------------------------------")
    username = input("Username: ")  # asks the user for their username and password
    password = input("Password: ")
    print("-----------------------------------------")
    clear()
    user_file = "".join([username, ext])
    user_file_path = os.path.join(User_path, user_file)
    if os.path.exists(user_file_path):
        fernet = Fernet(key)

        # opening the encrypted file
        with open(user_file_path, "rb") as enc_file:
            encrypted = enc_file.read()

        # decrypting the file
        decrypted = fernet.decrypt(encrypted)

        # opening the file in write mode and writing the decrypted data
        with open(user_file_path, "wb") as dec_file:
            dec_file.write(decrypted)
            dec_file.close()

        file = open(user_file_path, "r+")

        file.read()
        correct = False
        if username and password in user_file_path:
            correct = True  # if both the username and password are correct then correct is set to true

        if username and password not in user_file_path:
            correct = False  # if the username or password is wrong then correct stays the same

        if correct is True:
            if "User_Perm_Level: 1" in file:  # Team member (Ticket access only)
                os.environ["ENVIRO_USER_PERM_LEVEL"] = "1"

            if "User_Perm_Level: 2" in file:  # Manager/Admin/Team-Leader (Full access)
                os.environ["ENVIRO_USER_PERM_LEVEL"] = "2"
            enc(
                key_path, user_file_path
            )  # re encrypts the user file (I know it's very secure)

            os.environ["ENVIRO_USERNAME"] = username
            print(f"Welcome: {username}")  # prints a welcome message
            input("Press <ENTER> to continue")

        file.close
        clear()

    else:
        input(
            "Invalid Username and or Password\nPress <ENTER> to return to the main menu"
        )
        try:
            from Assignment_code.code.Return import back

            back()
        except ImportError as e:
            print(f"ERROR: {e}")


def enc(key_path, user_file_path):  # re-encrypts the data
    with open(key_path, "rb") as keyfile:
        key = keyfile.read()

    fernet = Fernet(key)

    with open(user_file_path, "rb") as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open(user_file_path, "wb") as encrypted_file:
        encrypted_file.write(encrypted)


login()
