import sys

from Assignment_code.code.Packages.clear import clear


def main():
    clear()
    try:
        pass
    except ImportError as e:
        print(f"ERROR: {e}\n")
        print(
            "PLEASE USE THE PROVIDED VENV VIRTUAL ENVIROMENT OR DOWNLOAD THE CRYPTOGRAPHY PACKAGE"
        )
        print(
            "MAKESURE THAT YOU ARE RUNNING PYTHON 3.12.1 OR NEWER. RUNNIN ANY OLDER PYTHON VERSION WILL CAUSE THE PROGRAM TO CRASH DUE TO HOW IT'S USE OF SOME FEATURES"
        )
        print(
            "If you wish to download the module use\n'pip install cryptogrpahy'\nor\n'python -m pip install cryptogrpahy'\nto install cryptography"
        )
        sys.exit()

    try:
        from Assignment_code.code.animation import animate_main

        # loads the animate program which has a loading screen
        animate_main()

    except ImportError as e:  # if it fails to load then it returns an error message
        print(f"ERROR: {e}")


if __name__ == "__main__":
    main()
