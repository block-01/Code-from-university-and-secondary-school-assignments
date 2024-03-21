import itertools
import sys
import threading
import time

from Assignment_code.code.Packages.clear import clear

# -----------
# ANIMATION:
# -----------


def animate_main():
    done = False

    def animate():
        clear()
        for c in itertools.cycle(
            ["(|)", "(/)", "(-)", "(\\)"]
        ):  # runs a loading animation
            if done:
                break
            sys.stdout.write("\rInitialising and running file check: " + c)
            sys.stdout.flush()
            time.sleep(0.1)

    t = threading.Thread(target=animate)
    t.start()

    # long process here
    time.sleep(3.5)  # makes it run for 3.5 seconds
    done = True
    clear()
    print("Program Initialised:")
    time.sleep(1)
    print("File Check complete:")
    time.sleep(
        1.5
    )  # displays the message "File Check Complete" and then runs the file check (this animation is just to look nice)


animate_main()
try:
    from Assignment_code.code.file_check import file_check

    file_check()
except ImportError as e:
    print(f"ERROR: {e}")
