file=open("Names.txt","w")
name=input ("Please enter a name")
file.write(name)
file.close()
file=open("Names.txt","r")
print (file.read())
file.close()
def yes_or_no(question):
    file=open("Names.txt","a")
    name=input ("Please enter a name")
    file.write (name)
    file.close()
    file=open("Names.txt","r")
    print (file.read())
    file.close()
    print ("Do you want to do it again")

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
    print(name)
else:
    print(name)
