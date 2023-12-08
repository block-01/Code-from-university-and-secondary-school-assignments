import csv 
print ("You have selected play:")
with open ("NEA_Dice_Game.csv","r") as f:
    playuser=input ("Please Input your Username.")
    playpassword1=input ("Please input your password.")
    playpassword2=input ("Please input your password again.")
if playpassword1==playpassword2:
    print ("Your password is correct")
 
csvreader = csv.reader(f, delimiter=",")
for row in csvreader:
    if "2016" in row[2]:
        print ("2016 spotted")
    



print ("You have selected play:")
    file=open ("NEA_Dice_Game.csv","r")
    playuser=input ("Please Input your Username.")
    playpassword1=input ("Please input your password.")
    playpassword2=input ("Please input your password again.")
    if playpassword1==playpassword2:
        print ("Your password is correct")
        print (Main_Game)
