#assign variables to a, b, c
a = 5
b = 13
c = -2

#compute each part of formula
b24ac = b**2 - 4*a*c
numerator1 = -b + b24ac ** 0.5
numerator2 = -b - b24ac ** 0.5
denominator = 2 * a

#obtain the two solutions
sol1 = numerator1 / denominator
sol2 = numerator2 / denominator

#print out the two solutions
print(sol1)
print(sol2)
