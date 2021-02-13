import numpy 
import copy 
from util import *
# Finding operator combinations with an operator tree


ANSWER = 7  # <--USER ENTERS DESIRED CARD THEY ARE TRYING TO GET TO HERE 
MYCARD_NAMES = ['4', '4', '8', '8', '9', '10', '10'] # <--USER ENTERS CARDS IN HAND HERE

MYCARDS = cards2nums(MYCARD_NAMES)


def graph(result, path, cards, root): # return generator of paths
    # recursively generate graph and take 7s 
    # depth = 0 -> result starts at adding card value 
    isFound = False

    if root:
        N_OPERATORS = 1
    else:
        N_OPERATORS = 8
    # different from depth 
        
    for C in cards: # different numbers available 
        for op in range(-1, N_OPERATORS): 
            # Get result at next node [[op, N]]
            if root:
                res = C
            else:
                res = operator(result, op, C)

            if res > 10000:
                continue
            # calculate next node result, but don't go there yet
            if res == ANSWER:
                P = path + [[op, C]] # append result at the node you just travelled to
                return P
                
            cards_copy = copy.deepcopy(cards)
            cards_copy.remove(C)
            if not isFound:
                if not cards_copy == []: # 
                    P = graph(res, path + [[op, C]], cards_copy, False)
                    if P != []:
                        return P
    return []
                    #for P in graph(res, path + [[op, C]], cards_copy, False): # THEN also append all results branching from the node you travelled to
                        
        
def formatEq(path):
    
    output = ""
    for i in range(len(path)):
        
        op = path[i][0]
        num = path[i][1] 
        
        if i == 0:
            output = num2card(num)

        else:
            if op == -1:
                output = output 
            elif op == 0: # res
                output = "(" + output + "+" + num2card(num) + ")"
            elif op == 1: # result = result - card
                output = "(" + output + "-" + num2card(num) + ")"
            elif op == 2: # result = card - result
                output = "(" + num2card(num) + "-" + output + ")"
            elif op == 3: # result = result - card
                output = "(" + output + "*" + num2card(num) + ")"
            elif op == 4: # result = result - card
                output = "(" + output + "/" + num2card(num) + ")"
            elif op == 5: # result = card - result
                output = "(" + num2card(num) + "/" + output + ")"
            elif op == 6: # result = result - card
                output = "(" + output + "^" + num2card(num) + ")"
            elif op == 7: # result = card - result
                output = "(" + num2card(num) + "^" + output + ")"
            elif op == 8: # result = result - card
                output = "(" + num2card(num) + "th root of " + output + ")"
            elif op == 9: # result = card - result
                output = "(" + output + "th root of " + num2card(num) + ")"
            elif op == 10: # result = result - card
                output = "(" + "log base " + num2card(num) + " of " + output + ")"
            elif op == 11: # result = card - result
                output = "(" + "log base " + output + " of " + num2card(num) + ")"
        
    return output + " = " + str(ANSWER)

def writePaths(path):
  
    with open('out.txt', 'w') as f:

        line = formatEq(path)
        print >> f, line

# ultimately returning the path and then writing recursive print function for the path
# outputting to text document 
def main():
    # Given MAX_DEPTH, ANSWERr
    print "Cards = ", MYCARDS
    print "PYTHON GO BRRRRR ..."

    for i in range(len(MYCARDS)):

        path = graph(0, [], MYCARDS, True) # operator paths to get to answer 
 
    if path is not None:
        print(path)
        writePaths(path)
    else:
        print "no paths found! :< better luck next time, comrade"
    return 0

main()