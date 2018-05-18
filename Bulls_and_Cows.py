def result(answer,guess):
    A = 0
    B = 0
    for idx_ans,val_ans in enumerate(answer):
        for idx_gue,val_gue in enumerate(guess):
            #print(inx_ans, val_ans, idx_gue, val_gue)
            if val_ans == val_gue:
                if idx_ans == idx_gue:
                    A += 1
                else:
                    B += 1
    return str(A)+'A'+str(B)+'B'

print(result('1234','4321'))
print(result('4567','9658'))
print(result('9876','6879'))