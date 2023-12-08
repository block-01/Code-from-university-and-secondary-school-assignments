import csv
import sys
again=file=open ("Passwords.Usernames.csv","a")
ans = input ("Do you wish to:\n 1)Create a new User ID\n 2)Change a password\n 3)Display all User IDs\n 4) Quit\n  (1/2/3/4) > ")
if ans == "1":
    print ("New User")
    user_list=["","","","",""]
    user_list.append(input("Please Enter a Username"))
    print("Your username","Has been added to the database")
    pswd_list=["password","null"]
    pswd_list.append(input("Please Enter a Password"))
    print ("press <ENTER> to continue")
again=input("Would you like to do it again Y or N")
file=open("Passwords.Usernames.csv","r")
while again=="Y":
    print(ans)



if ans == "2":
    changepasswordold1 = input("Please input your old password")
    if changepassword1 == pswd_list:
        print(changepassword2)
    changepasswordold2 = input("Can input your password again")
    if changepasswordold1==changepassword2:
            print ("Your old password is",changepasswordold2,changepasswordold1)
            newpassword1=input ("Please input your new pass word")
    else:
        print ("They are not the same")
        print (ans=="2")
if ans== "3":
    file=open ("Passwords.Usernames.csv","r")
    print (file.read)

elif ans== "4":
    print ("Thank you for using this program")
    file.close()
if again=="N":
    print ("Thank you for using this program")
    sys.exit
