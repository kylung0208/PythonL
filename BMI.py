def readInput():
    line1 = input()
    line2 = input()
    line3 = input()
    line4 = input()
    line1 = line1.strip()
    line2 = line2.strip()
    line3 = line3.strip()
    line4 = line4.strip()
    '''
    print(line1)
    print(line2)
    print(line3)
    print(line4)
    '''
    token1 = line1.split()
    token2 = line2.split()
    token3 = line3.split()
    token4 = line4.split()
    '''
    print(token1)
    print(token2)
    print(token3)
    print(token4)
    print(token2[3])
    print(type(token2[3]))
    '''

#calculate the BMI value
    BMIBob = (float(token2[3]))/((float(token2[2])/100)**2)
    BMIAlice = (float(token3[3]))/((float(token3[2])/100)**2)
    BMICharlie = (float(token4[3]))/((float(token4[2])/100)**2)
    '''
    print(BMIBob)
    print(BMIAlice)
    print(BMICharlie)
    '''
    
#this block identifies Bob's BMI Memo
    if BMIBob < 18.5:
        MemoBob = '體重過輕'
    elif BMIBob < 22.9:
        MemoBob = '正常範圍'
    elif BMIBob < 27:
        MemoBob = '過重'
    elif BMIBob < 30:
        MemoBob = '輕度肥胖'
    elif BMIBob < 35:
        MemoBob = '中度肥胖'
    else:
        MemoBob = '重度肥胖'

#this block identifies Alice's BMI Memo
    if BMIAlice < 18.5:
        MemoAlice = '體重過輕'
    elif BMIAlice < 22.9:
        MemoAlicemo = '正常範圍'
    elif BMIAlice < 27:
        MemoAlice = '過重'
    elif BMIAlice < 30:
        MemoAlice = '輕度肥胖'
    elif BMIAlice < 35:
        MemoAlice = '中度肥胖'
    else:
        MemoAlice = '重度肥胖'

#this block identifies Charlis's BMI Memo
    if BMICharlie < 18.5:
        MemoCharlie = '體重過輕'
    elif BMICharlie < 22.9:
        MemoCharlie = '正常範圍'
    elif BMICharlie < 27:
        MemoCharlie = '過重'
    elif BMICharlie < 30:
        MemoCharlie = '輕度肥胖'
    elif BMICharlie < 35:
        MemoCharlie = '中度肥胖'
    else:
        MemoCharlie = '重度肥胖'

#this block add BMI value to the list
    token1 += ['BMI','Memo']
    token2 += [float(token2[3])/(float(token2[2])/100)**2]
    token3 += [float(token3[3])/(float(token3[2])/100)**2]
    token4 += [float(token4[3])/(float(token4[2])/100)**2]
    '''
    print(token1)
    '''
#add Memo to the list
    token2 += [MemoBob]
    token3 += [MemoAlice]
    token4 += [MemoCharlie]


#Define and print out the format
    s1 = '{0:>8}{1:^11}{2:>6}{3:>7}{4:^10}{5:<7}'.format(token1[0],token1[1],token1[2],token1[3],token1[4],token1[5])
    print(s1)
    print('-' * 49)
    s2 = '{0:>8}{1:^11}{2:>6}{3:>7}{4:^10.2f}{5:<7}'.format(token2[0],token2[1],token2[2],token2[3],token2[4],token2[5])
    print(s2)
    s3 = '{0:>8}{1:^11}{2:>6}{3:>7}{4:^10.2f}{5:<7}'.format(token3[0],token3[1],token3[2],token3[3],token3[4],token3[5])
    print(s3)
    s4 = '{0:>8}{1:^11}{2:>6}{3:>7}{4:^10.2f}{5:<7}'.format(token4[0],token4[1],token4[2],token4[3],token4[4],token4[5])
    print(s4)

readInput()
