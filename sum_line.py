import sys 

def sum_lines():
    for line in sys.stdin:
        line = line.strip()
        print(line)
        tokens = line.split()
        print(tokens)
        print('Length: ',len(tokens))
        total = 0 
        for num in tokens:
            num = float(num)
            total = total + num 
        print('Total: ',total)
        print('Average: ',total/len(tokens))


sum_lines()

