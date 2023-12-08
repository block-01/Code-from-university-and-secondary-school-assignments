import csv
file = open("Stellaris.csv","w")
newn = input("What is the species name")
newa = input("What is the Homeworlds name")
newv = input("What is the Empire name")
newRecord = newn+","+newa+","+newv+"\n"
file.write(str(newRecord))
file.close()

