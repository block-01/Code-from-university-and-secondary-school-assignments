#Rules

print("Hello")
print("Rules:")
print("1. This is the most importyant rule....")
print("and that is to")
print("Have Fun")
print("2.Don't Cheat")
print("3.Don't argue over a go")
print("4.Don't tamper with the scores")
#player Names

Player1= input("Please input a name then press <Enter>")
Player2= input("Please input a name then press <Enter>")

print ("Player1 is",Player1,)
print ("Player2 is",Player2,)

#Game Start
print ("Type the grid reference to were you want to get the 0 or X to go")

def get_element(elements, x, y):
 
    return elements[x + (y * 10)]

def set_element(elements, x, y, value):
    
    elements[x + (y * 10)] = value


elements = []
for i in range(0, 100):
    elements.append(0)

i = 0
for x in range(0, 10):
    for y in range(0, 10):
        
        set_element(elements, x, y, i)
        i += 1

# First in first row.
print(get_element(elements, 0, 0, 0))
# Last in first row.
print(get_element(elements, 0, 0, 0))
# First in last row.
print(get_element(elements, 0, 0, 0))
