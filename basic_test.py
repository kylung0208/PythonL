x = [2,3,4]

#i is element
for i in x:
    print(i, end = ' ')
print(' ')

#i is position
for i in range(len(x)):
    print(x[i], end = ' ')
print()

#index(idx) & value  
# enumerate 函數！！！
for idx, i in enumerate(x):
    print(idx+1,i,sep=':')
print()

#append函數,put a new element to the bottom of the List
x.append(5)
print(x)

#List adding: z is a new list!
#if we just want to add simple things into the list, avoid using "+". (slow)
y = [1,2]
z = x + y
print(x,y,z,sep='\n')

#use append is a more simple manipulation # y is a list!
print('x.append(y)= ')
x.append(y)
print(x)
print(x[4])
print()

#Test: z & x is the same list !!
z = x
z[0] = 99
print(x,z,sep = '\n')

#print the last term of the list
print(x[len(x)-1])
print(x[-1])

#if we print x[-10], error appears! # the list is not long enough to count 10 terms form the bottom side!

#if we add 3 terms in 2 sapce ?!
print(x)
x[2:3] = [90,91,92]
print(x)
#Python will find the first space and add things into it 
#原本的後面順位往後一格!

