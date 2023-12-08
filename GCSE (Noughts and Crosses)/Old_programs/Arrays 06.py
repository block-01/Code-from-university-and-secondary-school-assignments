from array import*
nums = array('i',[])
for i in range (0,5):
    num = int(input("Enter a Whole Number"))
    nums.append(num)
nums =sorted(nums) 
nums.reverse()
print (nums)



