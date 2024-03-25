import sys

from Assignment_code.code.Packages.clear import clear


def exit():
    clear()
    yes = ["y", "Y"]
    no = ["n", "N"]
    check = input("Do you want to exit (Y/N): ")
    if check in no:
        input("Returning you to the main menu\nPress <ENTER> to continue")
        try:
            from Assignment_code.code.Return import back

            back()
        except ImportError as e:
            print(f"ERROR: {e}")

    if check in yes:
        # gives the user the option to return to the main menu if they selected the wrong option.
        input(
            "Thank you for using the ticket management program\nPress <ENTER> to continue"
        )
        clear()
        sys.exit(0)

    if check not in yes or no:
        input(
            "Invalid input\nReturning you to the main menu\nPress <ENTER> to continue"
        )
        try:
            from Assignment_code.code.Return import back

            back()
        except ImportError as e:
            print(f"ERROR: {e}")


exit()
