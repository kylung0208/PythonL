num1 = range(5,0,-1)
print(num1)
#'range' is diiferent from 'list'
# [ ] is defined in 'list'
# [ ] is not defined in 'range'
#so we can't write num1[2] = 100 , because [] isn't defined!!
nums = list(range(5,0,-1))
nums[2] = 100
print(nums)
# we can write nums[2] = 100 !!

#sum up numbers in the list!
a = [1,2,3]
total = 0
for el in a:
    total += el
print(total)

# We can use function 'sum' to acheive the same work!
total2 = sum(a)
print(total2)

# We can use func 'sum' to sum up range(5,0,-1)
total3 = sum(num1)
print(total3)

#For string:
# We can't modify a string, but we can modify a list!
strA = "Stone"
strA = list(strA)
strA[0] = "Y"
print(strA)
# If we want to turn a 'List' to 'String' ---> Use ' .join '
print(''.join(strA))
print(','.join(strA))