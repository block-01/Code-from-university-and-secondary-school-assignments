import os
import sys
from datetime import date, timedelta
from Assignment_code.code.Packages.clear import clear

"""
Inspiration has been taken from the Sample program on Canvas
for how this section of the program work such as the
ticket_delete and create_new functions and how the tickets
are saved and displayed which is in Dictionaries along with how
the datetime module is used.
"""

t_001 = {
    "blank": "",
    "ID": "001",
    "Title": "Print Hello World in python",
    "Description": "Create a script that prints Hello World",
    "Status": "Finished",
    "created_by": "System",
    "Assigned User": "Admin",
    "Date_Created": date.today() + timedelta(days=1),
    "Date_Updated": date.today() + timedelta(days=1),
}
t_002 = {
    "blank": "",
    "ID": "002",
    "Title": "Add Sprint Management",
    "Description": "Add sprint Management to the program",
    "Status": "Not Started",
    "created_by": "System",
    "Assigned User": "Admin",
    "Date_Created": date.today() + timedelta(days=1),
    "Date_Updated": date.today() + timedelta(days=1),
}
t_003 = {
    "blank": "",
    "ID": "003",
    "Title": "Run the program on Windows",
    "Description": "Get the program to work on windows",
    "Status": "Finished",
    "created_by": "System",
    "Assigned User": "Admin",
    "Date_Created": date.today() + timedelta(days=1),
    "Date_Updated": date.today() + timedelta(days=1),
}
t_004 = {
    "blank": "",
    "ID": "004",
    "Title": "Run the program on MacOS",
    "Description": "Get the program to work on MacOS",
    "Status": "Not Started",
    "created_by": "System",
    "Assigned User": "Admin",
    "Date_Created": date.today() + timedelta(days=1),
    "Date_Updated": date.today() + timedelta(days=1),
}
t_005 = {
    "blank": "",
    "ID": "005",
    "Title": "Run on a Raspberry PI",
    "Description": "Run the program on a Raspberry PI",
    "Status": "Finished",
    "created_by": "System",
    "Assigned User": "Admin",
    "Date_Created": date.today() + timedelta(days=1),
    "Date_Updated": date.today() + timedelta(days=1),
}
t_006 = {
    "blank": "",
    "ID": "006",
    "Title": "Reimpliment Team management",
    "Description": "Reimpliment the team management menu",
    "Status": "Not Started",
    "created_by": "System",
    "Assigned User": "Admin",
    "Date_Created": date.today() + timedelta(days=1),
    "Date_Updated": date.today() + timedelta(days=1),
}
t_007 = {
    "blank": "",
    "ID": "007",
    "Title": "Fix the Exit function",
    "Description": "Fix the error that exit has when going back into it",
    "Status": "Not Started",
    "created_by": "System",
    "Assigned User": "Admin",
    "Date_Created": date.today() + timedelta(days=1),
    "Date_Updated": date.today() + timedelta(days=1),
}
t_008 = {
    "blank": "",
    "ID": "008",
    "Title": "Port A-LEVEL NEA Game over to GODOT",
    "Description": "Port the game that was developed for my A-LEVE NEA from Defold over to GODOT",
    "Status": "In Progress",
    "created_by": "System",
    "Assigned User": "block_01",
    "Date_Created": date.today() + timedelta(days=1),
    "Date_Updated": date.today() + timedelta(days=1),
}
t_009 = {
    "blank": "",
    "ID": "009",
    "Title": "game artwork",
    "Description": "the games sprites and animations need to be redone",
    "Status": "Not Started",
    "created_by": "System",
    "Assigned User": "block_01",
    "Date_Created": date.today() + timedelta(days=1),
    "Date_Updated": date.today() + timedelta(days=1),
}
t_010 = {
    "blank": "",
    "ID": "010",
    "Title": "game music and sound effects",
    "Description": "Add music and sound effects to the game",
    "Status": "Not Started",
    "created_by": "System",
    "Assigned User": "block_01",
    "Date_Created": date.today() + timedelta(days=1),
    "Date_Updated": date.today() + timedelta(days=1),
}
data = {
    1: t_001,
    2: t_002,
    3: t_003,
    4: t_004,
    5: t_005,
    6: t_006,
    7: t_007,
    8: t_008,
    9: t_009,
    10: t_010,
}


def create_new(
    new_Title, new_Description
):  # create a new ticket (Idea gotten from the example code that was sent on canvas)
    for key in data:
        if data[key]["Title"] == new_Title:
            print("ERROR: Title must unique")
            create_new(new_Title, new_Description)

        if data[key]["Description"] == new_Description:
            print("ERROR: Title must unique")
            create_new(new_Title, new_Description)

    new_ID = len(data) + 1

    data[max(data.keys()) + 1] = {
        "blank": "",
        "ID": new_ID,
        "Title": new_Title,
        "Description": new_Description,
        "Status": "Not Started",
        "created_by": os.environ["ENVIRO_USERNAME"],
        "Assigned User": "N/A",
        "Date_Created": date.today() + timedelta(days=1),
        "Date_Updated": date.today() + timedelta(days=1),
    }
    print("Ticket has been saved")


def ticket_delete(key):
    # this function is called in main.py which when called deletes the ticket to the corispondin ID
    # insperation for how it works was taken from the sample program on Canvas
    del data[key]


def ticket_edit():  # Ticket edditing
    yes = ["Y", "y"]
    no = ["N", "n"]

    ID = int(input("Ticket ID: "))
    if ID in data:
        print("Current Ticket:")
        format_dict(ID)
        print("If you wish to leave a field the same, leave it blank and press <ENTER>")

        new_title_input = input("Title: ")
        new_description_input = input("Description: ")

        print(new_title_input)
        print(new_description_input)
        check = input("Do you wish to apply theses changes? (Y/N): ")
        if check in yes:
            if new_title_input != " ":
                data[ID].update({"Title": f"{new_title_input}"})
            if new_description_input != " ":
                data[ID].update({"Description": f"{new_description_input}"})
            clear()
            print("Changes Applied:")
            format_dict(ID)
            input("Press <ENTER> to continue")

        if check in no:
            input("Returning to ticket menu\nPress <ENTER> to continue")
            clear()
            try:
                from Assignment_code.code.Return import back
                back()

            except ImportError as e:
                print (f"ERROR: {e}")

        if check not in no or yes:
            input("Returning to ticket menu\nPress <ENTER> to continue")
            clear()
            try:
                from Assignment_code.code.Return import back
                back()

            except ImportError as e:
                print (f"ERROR: {e}")

    if ID not in data or ValueError:
        input("ERROR: Invalid Ticket ID\nPress <ENTER> to continue")
        clear()
        ticket_edit()


def read_ticket_details():  # Displays the full ticket if the entered ID is valid
    ID = int(input("Ticket ID: "))
    if ID in data:
        format_dict(ID)
        input("Press <ENTER> to continue:")
        clear()
        try:
            from Assignment_code.code.Return import back
            back()
        except ImportError as e:
            print (f"ERROR: {e}")

    if ID not in data or ValueError:
        input("ERROR: Invlaid Ticket ID\nPress <ENTER> to continue")
        read_ticket_details()


def change_ticket_status():  # allows for the ticket status to be changed depending on it's ID
    ID = int(input("Ticket ID: "))
    if ID in data:
        if data[ID]["Status"] == "Not Started":
            data[ID].update({"Status": "In Progress"})
            format_dict(ID)
            input("Press <ENTER> to continue")
            clear()
            return

        if data[ID]["Status"] == "In Progress":
            data[ID].update({"Status": "Finished"})

            format_dict(ID)
            input("Press <ENTER> to continue")
            clear()
            return

        if data[ID]["Status"] == "Finished":
            print("Ticket is done")
            format_dict(ID)
            input("Press <ENTER> to continue")
            clear()
            return

    if ID not in data or ValueError:
        input("Invalid Ticket ID\nPress <ENTER> to continue")
        change_ticket_status()

def ticket_assign_user(): # assigns a user to a ticket
    user_path = os.environ["ENVIRO_USER_PATH"]
    yes = ["Y", "y"]
    no = ["N", "n"]

    ID = int(input("Ticket ID: "))
    if ID in data:
        usernames_file_path = os.path.join(user_path, "Usernames.txt")
        if not os.path.exists(usernames_file_path):
            print (f"ERROR: No file at {usernames_file_path}")
            raise FileNotFoundError


        print ("Available Users:")
        file = open (usernames_file_path, "r")
        print (file)
        username = input("Username: ")
        if username in usernames_file_path:
            if data[ID]["Assigned User"] != "N/A":
                check = input (f"A User is already assigned to {data[ID]["Title"]}")

                if check in no:
                    input ("Returning to ticket menu\nPress <ENTER> to continue")
                    clear()

                if check not in no or yes:
                    print ("Invalid Input")
                    input ("Returning to ticket menu\nPress <ENTER> to continue")
                    clear()

            data[ID].update({"Assigned User": f"{username}"})
            print (f"{username} has been assigned to {data[ID]['Title']}")
            input ("Press <ENTER> to continue")
            file.close()
            clear()

        if username not in usernames_file_path:
            print (f"Unable to find user: {username}")
            input ("Press <ENTER> to continue")
            clear()
            file.close()
            ticket_assign_user()

    if ID not in data or ValueError:
        input("Invalid Ticket ID\nPress <ENTER> to continue")
        ticket_assign_user()

# -----------------------------
# DICTIONARY OUTPUT (FORMATED):
# -----------------------------


# formats and outputs a section of the table
def Table_output_full_formated():  # Taken code and modified from Example program on Canvas
    print("")
    table_headings = ["ID", "Title", "Status", "created_by", "Assigned user", "Date_created"]
    print(
        f"|{table_headings[0]:6}|{table_headings[1]:40}|{table_headings[2]:13}|{table_headings[3]:12}|{table_headings[4]:13}|{table_headings[5]:13}|"
    )

    for ID in data:

        print(
            f"|{data[ID]['ID']:5} "
            f"|{data[ID]['Title']:40}"
            f"|{data[ID]['Status']:13}"
            f"|{data[ID]['created_by']:12}"
            f"|{data[ID]['Assigned User']:13}"
            f"|{data[ID]['Date_Created']:%d-%m-%y:15}  |"
        )


# formats and outputts a small part of the dictionary


def format_dict(ID):
    table_headings = [
        " ",
        "ID",
        "Title",
        "Description",
        "Status",
        "created by",
        "Assigned user|"
        "Date created",
        "Date updated",
    ]
    print(
        f"{table_headings[0]:0}|{table_headings[1]:8}|{table_headings[2]:40}|{table_headings[3]:50}|{table_headings[4]:8}|{table_headings[5]:13}|{table_headings[6]:10}|{table_headings[7]:10}|"
    )

    print(
        f"{data[ID]['blank']:1}"
        f"|{data[ID]['ID']:8}"
        f"|{data[ID]['Title']:40}"
        f"|{data[ID]['Description']:50}"
        f"|{data[ID]['Status']:8}"
        f"|{data[ID]['created_by']:13}"
        f"|{data[ID]['Assigned User']:13}"
        f"|{data[ID]['Date_Created']:%d-%m-%y:24} "
        f"|{data[ID]['Date_Updated']:%d-%m-%y:10} |"
    )
