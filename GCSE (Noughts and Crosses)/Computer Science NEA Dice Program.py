import math
import csv  # This is used for  the file system in the program
import random  # This is used for the main dice part of the program
import sys  # This is used to call the code in the elif == "6" statement to quit the program.

def main(): #this is were the main game is intended to start from atleast if it works.
    file=open ("NEA-Scores.csv","a")
    print ("Playing Game")

    score1=0

    score2=0

    print ("Do you want to veiw the rules again. Please Type Y or N")
    question01=input ("") 
    if question01 == "y":
        print ("Rules:\n 1)Both players have 5 go's each.\n 2)After that if you both have the same amount of points you will both role again.\n 3)If you role an odd number you lose 5 points and if you role an even number you gain 10 points.")  
    else:
        for i in range (0,5):
            print("Rolling player01's first dice")
            Player01A=random.randint(0,6)
            print("Your first number is",Player01A)
            Player01B=random.randint(0,6)
            print("your second number is",Player01B)
            total01= Player01A+Player01B
            print("The sum of your number is",total01)
            if (total01 % 2) == 0:
                print ("you have gained 5 points")
                score1 = score1 + 5 
                print (score1)

            else:
                print ("You have lost 5 points")
                score1 = score1 - 5
                print (score1)
            if score1=="0":
                print ("you have not lost any points(reason you are at 0 points)")
                
            cont=input ("Please press <ENTER> to continue")

            print("Rolling player02's first dice")
            Player02A=random.randint(0,6)
            print("Your first number is",Player02A)
            Player02B=random.randint(0,6)
            print("your second number is",Player02B)
            total02= Player02A+Player02B
            print("The sum of your number is",total02)
            if (total02 % 2) == 0:
                print ("you have gained 5 points")
                score2 = score2 + 5 
                print (score2)

            else:
                print ("You have lost 5 points")
                score2 = score2 - 5
                print (score2)
            if score2=="0":
                print ("you have not lost any points(reason you are at 0 points)")
                
            newRecord = score1+","+score2+""
            file.write(str(newRecord))
            file.close()

            if score1==score2: #this checks to see if the score is the same if it is then the program runs the game a last time.
                print("Rolling player01's first dice")
                Player01A=random.randint(0,6)
                print("Your first number is",Player01A)
                Player01B=random.randint(0,6)
                print("your second number is",Player01B)
                total01= Player01A+Player01B
                print("The sum of your number is",total01)
                if (total01 % 2) == 0:
                    print ("you have gained 5 points")
                    score1 = score1 + 5 
                    print (score1)

                else:
                    print ("You have lost 5 points")
                    score1 = score1 - 5
                    print (score1)
                if score1=="0":
                    print ("you have not lost any points(reason you are at 0 points)")
                    
                cont=input ("Please press <ENTER> to continue")

                print("Rolling player02's first dice")
                Player02A=random.randint(0,6)
                print("Your first number is",Player02A)
                Player02B=random.randint(0,6)
                print("your second number is",Player02B)
                total02= Player02A+Player02B
                print("The sum of your number is",total02)
                if (total02 % 2) == 0:
                    print ("you have gained 5 points")
                    score2 = score2 + 5 
                    print (score2)

                else:
                    print ("You have lost 5 points")
                    score2 = score2 - 5
                    print (score2)
                if score2=="0":
                    print ("you have not lost any points(reason you are at 0 points)")


#def ansback():
file=open ("NEA_Dice_Game.csv","r")
file=rows=['Username','Password','Score']
print ("☃")
print ("Welcome to my Computer Science NEA Programming Project Dice game")
ans = input ("Do you wish to:\n 1)Play\n 2)Create new user ID\n 3)Display all scores\n 4)Display all usernames\n 5)Display Rules and Game Infomation6)Quit\n (1/2/3/4/5/6) > ")

if ans == "1":
    #The play option requires the input of a username and password to use.
    print ("You have selected play:")
    file=open ("NEA_Dice_Game.csv","r")
    with open ("NEA_Dice_Game.csv","r") as r:
        playuser=input ("Please Input your Username.")
        csvreader = csv.reader(r,delimiter=",")
        for row in csv.reader(r,delimiter=","):
            if "playuser" in row:
                print ("User Accepted")
            else:
                print ("There is no user under this name.") # this is printed if there is no user under the enrtred name on the the file.
            
            playpassword1=input ("Please input your password.")
            playpassword2=input ("Please input your password again.")
            if playpassword1==playpassword2:
                print ("Your password is correct.") 
                main()
            else:
                print ("There is no such user in the database please try again later.")
                print ("")
                
if ans== "2":
            #Allows the user to create a new username and password so that they can then play the game.
    print ("Creating New User:")
                
    file=open ("NEA_Dice_Game.csv","a")
    newusername=input("Please input a username")
    newpassword=input("Please input a password")
    newpassword2=input("Please input the password again")
    if newpassword==newpassword2:
        newRecord = newusername+","+newpassword+""
        file.write(str(newRecord))
        file.close()
        print ("New Username and Password Accepted")    
        reans=input ("Do you wish to go back to the start.")
        #ansback()
    else:
        print ("Your second inputed password was not the same as the first one.")
                
if ans== "3":
            #Displays the username and their highscore from largest (at the top of the list) to smallest (smallest at the bottom of the list)
    print ("Displaying Hall of Fame:")
    file= open ("NEA_Dice_Game.csv","r") 
    file.read
    contents= file.read()
    print (contents)
    file= open ("NEA-Scores.csv","r")
    file.read
    score = file.read()
    print(score)
    #ansback()
            
if ans== "4":
            #this displays all the usernames on the file
    print ("Dislplaying all Usernames on record:")
    file= open ("NEA_Dice_Game.csv","r") 
    file.read
    contents= file.read()
    print (contents)
    #ansback()

if ans=="5":
        # if the user choices this option then the program will display the rules.
    print ("Displaying Rules and Game Infomation:")
    print ("Rules:\n 1)Both players have 5 go's each.\n 2)After that if you both have the same amount of points you will both role again.\n 3)If you role an odd number you lose 5 points and if you role an even number you gain 10 points.")
        #ansback()
        
elif ans== "6":
        #if the user choices to exit the program then the sys.exit kills the program.
    print ("Thank you for playing.")
    sys.exit