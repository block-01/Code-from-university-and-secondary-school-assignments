import csv
import random
import sys
file= open ("Details.csv","a")
username= input ("Please enter a username")
for x in range(2):
    print (random.randint(1,51))
    print
file.close()
file=open ("Details.csv","r")
print (file.read())
file.close()
ans=input("Would you like to do it again Y is yes and N is No")
c=file=open("Details","a")
while ans=="Y":
 
    if ans=="N":
        print ("Thank you for using this program")
        file.close()
        sys.exit
    
    file=open("Details.csv","a")
    username1= input ("Please enter a username")
    for x in range(2):
        print (random.randint(1,51))
        print
    file.close()
    file=open ("Details.csv","r")
    print (file.read())
    file.close()
    ans2=input("Would you like to do it again y is yes and N is No")

file=open("Details.csv","r")
while ans2=="y":
    print(c)
    file.close()


if ans2=="N":
    print ("Thank you for using this program")
