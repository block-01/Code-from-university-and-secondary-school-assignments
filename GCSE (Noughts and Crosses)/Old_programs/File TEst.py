#for py 2.x input should be raw_input
input1 = input("first input:")
input2 = input("second input:")
file = open("somefile.txt", "w")
file.write(input1 + "\n") #the \n is the line separator (on unix, might be different in windows/mac os)
file.write(input2 + "\n")
print (input1,\n,input2)
file.close()
