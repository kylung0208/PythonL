#encoding:utf-8
x = 1234
myformat = 'integers: %d | %-6d | %06d'
print(myformat % (x, x, x))

#try 2
y, z = (1.23456789, 123456789)
myfomat2 = 'output: %e | %E | %f | %g'
print(myfomat2 % (y, y, y, y))
print(myfomat2 % (z, z, z, z))

#try 3 
myformat3 = 'output2: %-6.2f | %05.2f | %+06.1f'
print(myformat3 % (y, y, y))
