from os import name, system


def clear():
    # checks what operating system kernel is running and then runs clear
    # if it is unix based (Linux and MAC-OS) or if it is NX (Windows)
    # based then it runs cls
    if name == "nt":
        # nt is windows if it detects that windows is running it will run the command "CLS" which will wipe the console
        _ = system("cls")

    # if it detect that MacOS or an operating system using the linux Kernel is running then it will run the "clear" command which will clear the console.
    else:
        _ = system("clear")
