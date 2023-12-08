import random 

messages = [ 
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
]

while True:
    print ("This is a Dice.To prossed press <ENTER>")
    input ()

    message = random.choice(messages) 
    print (message) 

    input ("Press <ENTER> to continue")
    for i in range (100) : 
        print ("\n")       

