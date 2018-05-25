#請由輸入讀取班上每個同學的出生月份, 然後將每個月份的人數印出.
#輸入的每一行代表一個學生的座號和生日月份.
import sys
def test():
    for line in sys.stdin:
        line = line.strip()
        print(line)


def month():
    Jan = 0
    Feb = 0
    Mar = 0
    Apr = 0
    May = 0
    Jun = 0
    Jul = 0
    Aug = 0
    Sep = 0
    Oct = 0
    Nov = 0
    Dec = 0
    for line in sys.stdin:
        line = line.strip()
        tokens = line.split()
        if int(tokens[1]) == 1:
            Jan += 1 
        if int(tokens[1]) == 2:
            Feb += 1
        if int(tokens[1]) == 3:
            Mar += 1
        if int(tokens[1]) == 4:
            Apr += 1
        if int(tokens[1]) == 5:
            May += 1
        if int(tokens[1]) == 6:
            Jun += 1
        if int(tokens[1]) == 7:
            Jul += 1
        if int(tokens[1]) == 8:
            Aug += 1
        if int(tokens[1]) == 9:
            Sep += 1 
        if int(tokens[1]) == 10:
            Oct += 1
        if int(tokens[1]) == 11:
            Nov += 1
        if int(tokens[1]) == 12:
            Dec +=1
    print('1',Jan)
    print('2',Feb)
    print('3',Mar)
    print('4',Apr)
    print('5',May)
    print('6',Jun)
    print('7',Jul)
    print('8',Aug)
    print('9',Sep)
    print('10',Oct)
    print('11',Nov)
    print('12',Dec)
month()


# Use Dictionary can reach a better method (fewer lines)
def goodway():
    birthdays = {}
    for line in sys.stdin:
        line = line.strip()
        tokens = line.split()
        print(tokens)
        m = int(tokens[1])
        if birthdays.get(m):
            birthdays[m] += 1
    #print birthdays
    for i in range(1,13):
        print(i,birthdays.get(i))
# Still have some bugs ?!