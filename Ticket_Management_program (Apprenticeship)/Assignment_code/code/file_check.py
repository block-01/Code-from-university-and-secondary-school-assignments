import os
import sys

try:
    from cryptography.fernet import Fernet
except ImportError as e:
    print(f"ERROR: {e}\nRUN THIS PROGRAM WITH THE PROVIDED VENV ENVIROMENT")
# ------------
# FILE CHECK:
# ------------


def file_check():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    os.chdir("../")

    # This script checks that the directories that contain the tickets exist,
    # if they don't exist the program creates them.

    if not os.path.exists("File_Structure"):
        try:
            os.mkdir("File_Structure")
        except OSError or PermissionError as e:
            print(
                f"ERROR: {e}"
            )  # if it is unable to create the directories then the exception is triggered
            sys.exit()

    os.chdir("File_Structure")

    if not os.path.exists("Output_Logs"):
        try:
            os.mkdir("Output_Logs")
        except OSError or PermissionError as e:
            print(
                f"ERROR: {e}"
            )  # if it is unable to create the directories then the exception is triggered
            sys.exit()

    if not os.path.exists("User_data"):
        try:
            os.mkdir("User_data")
        except OSError or PermissionError as e:
            print(
                f"ERROR: {e}"
            )  # if it is unable to create the directories then the exception is triggered
            sys.exit()

    if not os.path.exists("Data"):
        try:
            os.mkdir("Data")
        except OSError or PermissionError as e:
            print(
                f"ERROR: {e}"
            )  # if it is unable to create the directories then the exception is triggered
            sys.exit()

    if not os.path.exists("Data/key.key"):
        try:
            os.chdir("Data/")
            key = Fernet.generate_key()  # generates the encryption key

            with open("key.key", "wb") as filekey:
                filekey.write(key)  # saves the encryption key
            os.chdir("../")
        except ChildProcessError or PermissionError as e:
            print(
                f"ERROR: {e}"
            )  # if it is unable to create the directories or write to the file then the exception is triggered
            sys.exit()

    if not os.path.exists(".gitignore"):
        try:
            file = open(".gitignore", "w")
            file.write("*")
            file.close()
        except ChildProcessError or PermissionError as e:
            print(f"ERROR: {e}")
            sys.exit()

    # Assigns the directions and files that are created a enviroment variable so that
    # they can easily be called by other python scripts in the program
    try:
        os.environ["ENVIRO_OUTPUT_PATH"] = os.path.join(
            os.getcwd(), "Output_Logs/"
        )  # where output logs are saved
        os.environ["ENVIRO_USER_PATH"] = os.path.join(
            os.getcwd(), "User_data/"
        )  # where user data is saved
        os.environ["ENVIRO_TICKETS_PATH"] = os.path.join(os.getcwd(), "Tickets/")
        os.environ["ENVIRO_DATA_PATH"] = os.path.join(os.getcwd(), "Data/")
        os.environ["ENVIRO_KEY_PATH"] = os.path.join(
            os.getcwd(), "Data/key.key"
        )  # where the encryption is saved (not secure (need to change))
        os.environ["ENVIRO_FILE_STRUCTURE"] = (
            os.getcwd()
        )  # the root directory of where all of the data for the program is saved

    except (
        OSError or EnvironmentError or KeyError
    ) as e:  # if there is an error saving the environment variables then this exception is triggered
        print(f"ERROR: {e}")

    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    try:
        from Assignment_code.code.main import main_menu

        main_menu()
    except ImportError or ImportWarning as e:
        print(f"ERROR: {e}")
