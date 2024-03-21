import os

import Assignment_code.code.Packages.data as data
from Assignment_code.code.Packages.clear import clear

# -----------
# MAIN MENU:
# -----------


def main_menu():
    # checks that File check has been ran and that the file paths are valid
    try:
        print(os.environ["ENVIRO_DATA_PATH"])
        print(os.environ["ENVIRO_USER_PATH"])
        print(os.environ["ENVIRO_KEY_PATH"])
    except OSError or Exception or KeyError as e:
        print("SYSTEM FAILURE: ONE OR MORE ENVIROMENT VARIBALES NOT FOUND")

        print("ERROR: FILE_CHECK.PY HASN't BEEN RAN, HAS FAILED OR IS NON EXISTANT")
        print(f"ERROR: {e}")

    print("TEST: Startup Complete")

    clear()

    valid = ["1", "2", "3", "4"]

    print(
        "/==========================\\ \n|Ticket Management Software|\n\\==========================/"
    )
    data.Table_output_full_formated()
    print(
        """
-----------------------------------------
Main menu:
-----------------------------------------
1) Tickets:
-----------------------------------------
2) User menu:
-----------------------------------------
3) Exit:
-----------------------------------------
"""
    )

    menu = input(": ")

    if (
        menu == "1"
    ):  # option selected if the user wants to edit, delete, update the status or create a new ticket
        clear()
        ticket_menu()

    if (
        menu == "2"
    ):  # option selected if the user wants to change settings or add or create teams and users
        clear()
        try:  # trys to load the User settings menu if it fails it returns an exception and an error message
            from Assignment_code.code import User

            User()
        except ImportError:
            try:
                import User

                User()
            except ImportError as e:
                print(f"ERROR: {e}")

    if menu == "3":  # option selected if the user wants to exit out of the program
        clear()
        try:
            from Assignment_code.code.Exit import exit

            exit()
        except ImportError as e:
            print(f"ERROR: {e}")

    if menu is not valid:
        input("That wasn't an option\nPress <ENTER> to continue")
        main_menu()


# -------------
# TICKET MENU:
# -------------


def ticket_menu():
    clear()
    valid = ["0", "1", "2", "3", "4", "5", "6"]
    print(
        """
------------------------------------------
Ticket menu:
Please enter a number:
------------------------------------------
1) Create a new Ticket: (account required)
------------------------------------------
2) Edit a Ticket: (account required)
------------------------------------------
3) Delete a Ticket: (account required)
------------------------------------------
4) Search for a ticket:
------------------------------------------
5) Change Status: (account required)
------------------------------------------
6) Assign User: (account required)
------------------------------------------
7) Return to main menu:
------------------------------------------
"""
    )
    menu = input(": ")

    if menu == "1":  # option selected if the user wants to create a new ticket
        clear()
        try:
            from Assignment_code.code.Packages.Login import login

            login()  # to create a new ticket the user has to have a user account
        except ImportError:
            try:
                from Packages.Login import login

                login()
            except ImportError as e:
                print(f"ERROR: {e}")
        clear()
        new_Title = input("Ticket name: ")
        new_Description = input("Ticket description: ")
        data.create_new(new_Title, new_Description)
        clear()
        main_menu()

    if menu == "2":  # option selected if the user wants to edit a ticket
        clear()
        try:
            from Assignment_code.code.Packages.Login import login

            login()  # to edit a ticket the user has to have a user account
        except ImportError as e:
            print(f"ERROR: {e}")
        data.ticket_edit()
        clear()
        ticket_menu()

    if menu == "3":  # option selected if the user wants to remove a ticket
        try:
            from Assignment_code.code.Packages.Login import login

            login()  # to delete a ticket the user has to have a user account
        except ImportError:
            try:
                from Packages.Login import login

                login()
            except ImportError as e:
                print(f"ERROR: {e}")

        delete_ticket_menu()
        clear()
        ticket_menu()

    if menu == "4":
        data.read_ticket_details()
        clear()
        ticket_menu()

    if menu == "5":
        try:
            from Assignment_code.code.Packages.Login import login

            login()  # to delete a ticket the user has to have a user account
        except ImportError as e:
            print(f"ERROR: {e}")

        data.change_ticket_status()
        clear()
        ticket_menu()

    if menu == "6":
        try:
            from Assignment_code.code.Packages.Login import login

            login()
        except ImportError as e:
            print(f"ERROR: {e}")
        data.ticket_assign_user()

    if menu == "7":  # returns the user to the main menu
        clear()
        main_menu()

    if menu not in valid:
        input("That wasn't a valid option\nPress <ENTER> to continue")
        ticket_menu()


# ---------------------
# TICKETING FUNCTIONS:
# ---------------------


def delete_ticket_menu():  # Ticket deletion

    clear()
    print("Press <ENTER> to return to the main menu without entering any string")
    ticket_id = input("Ticket ID: ")
    print(ticket_id)
    if ticket_id in data.data:
        print("This action is not revesable.\nDo you wish to continue (Y/N)")
        check = input(": ")

        valid_yes = ["Y", "y"]
        valid_no = ["N", "n"]

        if check in valid_yes:
            data.ticket_delete()
            input(
                f"{ticket_id} has been deleted\nReturning to ticket menu\nPress <ENTER> to continue"
            )
            print("Del")
            clear()
            ticket_menu()

        if check in valid_no:
            input("Returning to ticket menu\nPress <ENTER> to continue")
            ticket_menu()

        if check not in valid_no or valid_yes:
            print("Invalid input")
            input("Press <ENTER> to continue.")

    if ticket_id not in data.data:
        input("ERROR: Invalid Ticket ID\nPress <ENTER> to continue")
        delete_ticket_menu()


main_menu()
