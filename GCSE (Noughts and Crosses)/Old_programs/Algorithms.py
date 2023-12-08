print ("Welcome to ")
Code1=input ("Please enter a 5 character product code that starts with AB or AS followed by 3 numerical numbers.")

print ("Do you want to place another order if not type NA in the option boxes bellow")

def yes_or_no(question):
    answer = input(question + "(y/n): ").lower().strip()
    print("")
    while not(answer == "y" or answer == "yes" or \
    answer == "n" or answer == "no"):
        print("Input yes or no")
        answer = input(question + "(y/n):").lower().strip()
        print("")
    if answer[0] == "y":
        return True
    else:
        return False

if yes_or_no("Ayy?"):
    print("")
else:
    print(Code1)
