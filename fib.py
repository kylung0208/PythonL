#1 1 2 3 5 8 13 ...
#fib(3) -> 2
#fib(5) -> 5

def fib(n):
    a, b = 0, 1
    for i in range(1, n):
        a, b = b, a+b
    return b 

print(fib(3))
print(fib(5))
print(fib(7))

def fib2(n):
    a = 0
    b = 1
    for i in range(1,n):
        c = a + b
        a = b 
        b = c
    return b

print(fib2(3))
print(fib2(5))
print(fib2(7))