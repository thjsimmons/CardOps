import numpy as np

'''
    Operator List: (12 operations)
    0 A + B

    1,2 A - B, B - A
    
    3, A * B

    4,5, A / B, B / A
    
    6,7, A^B, B^A

    8,9, A^(1/B), B^(1/A)

    10, 11 logA(B), logB(A)    


'''

def operator(result, op, N):
    A = result 
    B = N
    res = result
    if op == -1:
        res = A
    if op == 0: # addition
        res = A + B
    if op == 1: # subtraction, non-commutative
        res = A - B
    if op == 2: # multiplication
        res = B - A
    if op == 3: # division, non-commutative
        res  = A * B
    if op == 4:
        if B != 0:
            res = A/float(B)
        else:
            res = 9999999999
    if op == 5:
        if A != 0:
            res = B/float(A)
        else:
            res = 9999999999
    if op == 6:
        if B > 80:
            res = 9999999999
        else:
            res = A**B
    if op == 7:
        if A > 80:
            res = 9999999999
        else:
            res = B**A
    if op == 8:
        if B != 0:
            res = A**(1/float(B)) if A >= 0 else 99999999
        else:
            res = 9999999999
    if op == 9:
        if A != 0:
            res = B**(1/float(A)) if A >= 0 else 99999999
        else:
            res = 9999999999
    if op == 10:
        if np.log(B) != 0:
            res = np.log(abs(A)) / np.log(abs(B))
        else:
            res = 9999999999
    if op == 11:
        if np.log(A) != 0:
            res = np.log(abs(B)) / np.log(abs(A))
        else:
            res = 9999999999
    return res
    
def op2str(op): # fails for commutative operators
    strs = ["+", "-", "*", "/"]
    return strs[op]

def num2card(num):
    # num in set (1-14, range(1,15)
    # "A" is 1 and 14
    # index 0-13
    cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    return cards[num-1]

def cards2nums(cards):
    output = []
    for card in cards:
        if card == "A":
            output.append(1)
        elif card == "K":
            output.append(13)
        elif card == "Q":
            output.append(12)
        elif card == "J":
            output.append(11)
        else:
            output.append(int(card))
    return output
