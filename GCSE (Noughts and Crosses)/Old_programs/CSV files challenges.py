import csv
file= open("Books.csv","w")
file.write("To kill a Mocking By Harper Lee Released 1960\n")
file.write("A Brief History of Time By Stephen Hawking Released 1988\n")
file.write("The Great Gatsby by F.Scott Fitzgerald Released 1922zn")
file.write("The Man Who Mistook His Wife for a Hat by Oliver Sacks Released 1985\n")
file.write("Pride and Prejudice By Jane Austen Released 1813\n")
file.close()
file = open("Books.csv","r")
print (file.read())
file.close()

for i in range (0,10):
#for ans=="yes":
        file=open("Books.csv","a")
        book= input("Enter the name of a Book")
        author=input("Enter the name of the Author")
        year=input("Enter the year that the book was released")
        newRecord = book+","+author+"Released"+year+"\n"
        file.write(str(newRecord))
        file.close()
        file = open("Books.csv","r")
        print (file.read())
        file.close()
        #ans=input("Do you wish to continue and do it again type yes or no and press <ENTER>")
        #else: ans == "no"
            #print("Thank you for the information!")    
