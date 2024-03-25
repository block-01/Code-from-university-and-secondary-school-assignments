import os

from Assignment_code.code.Packages.clear import clear
from cryptography.fernet import Fernet


def user_menu():
    signin = 0

    try:
        Data_path = os.environ["ENVIRO_DATA_PATH"]
        User_path = os.environ["ENVIRO_USER_PATH"]
        key_path = os.environ["ENVIRO_KEY_PATH"]
    except OSError or EnvironmentError as e:
        print(f"ERROR: {e}")
    valid = ["1", "2", "3", "4"]
    print("User managment menu:")

    print(
        """
Please enter a number:
-------------------------------------------------------
1) Create a new user (Level-3 (Admin/Team operation)):
-------------------------------------------------------
2) Remove User (Level-3 (Admin/Team Leader operation)):
-------------------------------------------------------
3) Help:
-------------------------------------------------------
4) Exit menu:
-------------------------------------------------------"""
    )
    user_menu = input(": ")

    if user_menu == "1":
        try:
            from Assignment_code.code.Packages.Login import login

            login()
        except ImportError as e:
            print(f"ERROR: {e}")
        new_user(User_path, Data_path, key_path, signin)

    if user_menu == "2":
        try:
            from Assignment_code.code.Packages.Login import login

            login()
        except ImportError as e:
            print(f"ERROR: {e}")
        user_remove(User_path)

    if user_menu == "3":
        clear()
        help_menu()

    if user_menu == "4":
        input("Returning you to the main menu\nPress <ENTER> to continue")
        clear()
        try:
            from Assignment_code.code.Return import back

            back()
        except ImportError as e:
            print(f"ERROR: {e}")

    if user_menu not in valid:
        input("That wasn't an option\nPress <ENTER> to continue")
        user_menu()


def new_user(User_path, Data_path, key_path, signin):
    ext = ".txt"
    n = """

"""
    clear()
    print("New user:\n")

    os.chdir(User_path)
    user_file = open("Usernames.txt", "a+")

    new_username = input("Please enter a new username: ")
    if " " in new_username:
        print(
            """
Please try again:
The username cannot contain any spaces please use a '_' or a '-' instead
            """
        )
        input("Press <ENTER> to continue")
        clear()
        new_user(User_path, Data_path, key_path, signin)

    while new_username not in user_file:
        user_file.write(new_username)
        user_file.write(n)
        user_file.close
        user_file = "".join([new_username, ext])
        new_user_file = open(user_file, "a+")
        new_user_file.write(new_username)

    new_user_pswd = input("Please enter a password for the new user: ")
    pswd2 = input("Please enter your password again: ")
    if new_user_pswd == pswd2:
        file = open(user_file, "a")
        file.write(n)
        file.write(
            """

                   """
        )
        file.write(pswd2)
        file.close()
    else:
        print("The passwords do not match")
    print("User permission Level")
    print(
        """
---------------------------
Enter 1 for Team Member:
---------------------------
Enter 2 for a Team Leader:
---------------------------"""
    )
    user_perm_level = input(": ")

    if user_perm_level == "1":
        new_user_file.write(
            """

User_Perm_Level: 1"""
        )

    if user_perm_level == "2":
        new_user_file.write(
            """

User_Perm_Level: 2"""
        )

    with open(key_path, "rb") as keyfile:
        key = keyfile.read()

    fernet = Fernet(key)

    with open(user_file, "rb") as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open(user_file, "wb") as encrypted_file:
        encrypted_file.write(encrypted)
    print("New user created")
    check = input(
        f"User: {new_username} has been added\nDo you want to create another user?(Y/N)"
    )
    valid_yes = ["Y", "y"]
    valid_no = ["N", "n"]
    if check in valid_yes:
        signin = 1

        new_user(User_path, Data_path, key_path, signin)

    if check in valid_no:
        input("Returning you to the user menu\nPress <ENTER> to continue.")
        clear()
        user_menu()
    if check not in valid_no or valid_yes:
        input("Invalid Input\nReturning to user menu\nPress <ENTER> to continue")


def user_remove(User_path):  # admin level user can remove other users except it's self
    clear()
    name = input("Username:")
    user_file = User_path + f"{name}.txt"

    while (
        not os.path.exists(user_file) or name == "Usernames" or "Admin"
    ):  # if the username doesn't exist or is the usernames.txt file then it will enter the while loop
        print("Invalid Username")
        name = input("Username:")
        user_file = User_path + f"{name}.txt"
    print(
        f"WARNING: deleting '{name}' is a process that cannot reversed\nDo you wish to continue (Y/N)"
    )
    check = input(": ")

    if check != "Y":
        input("Returning you to menu\nPress <ENTER> to continue")
        user_menu()

    try:
        os.remove(user_file)
    except OSError or PermissionError as e:
        print(f"ERROR: {e}, with deleting user {name}")

    clear()
    input(f"{name} has been deleted\nPress <ENTER> to continue")
    clear()
    check = input("Do you want to delete another user? (Y/N)")

    valid_yes = ["Y", "y"]
    valid_no = ["N", "n"]

    if check in valid_no:
        clear()
        input("Returning to user menu\nPress <ENTER> to continue")
        clear()
        user_menu()

    if check in valid_yes:
        clear()
        user_remove(User_path)

    if check not in valid_no or valid_yes:
        input("Invalid input\nReturning to user menu\nPress <ENTER> to continue")


def help_menu():
    print(
        """
----------------------------------------------
User Levels:
----------------------------------------------
Admin (Level-02):
----------------------------------------------
Full read and write,
User creation,
User Deletion,
Ticket Creation,
Ticket Editing,
Ticket Viewing,
----------------------------------------------
Team member (Level-01):
----------------------------------------------
Ticket Creation,
Ticket Editing,
Ticket Viewing,
----------------------------------------------
Guest(Level-0)(No account required (Default)):
----------------------------------------------
Viewing current and past tickets,
and Active Users,
----------------------------------------------"""
    )
    input("Press <ENTER> to return to the user menu")
    clear()
    user_menu()


user_menu()
