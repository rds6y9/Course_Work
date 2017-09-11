####################################################
# Programmer: Ryan Stoughton
# Class: CS5200
# Assignment: 2
# File: assignment2.py
####################################################


############### Problem 1 ###################
# See assignment2.doc
#############################################


############### Problem 2 ###################
def f(n):
    if n <= 0:
        return 0
    else:
        return f(n-1) + (n**2 / (((2 * n) - 1) * ((2 * n) + 1)))

def g(n):
    if n <= 0:
        return 0
    else:
        return ((n * (n + 1)) / (2 * ((2 * n) + 1)))

def p(n):
    return '%.6f'%(f(n)) == '%.6f'%(g(n))
##############################################


############### Problem 3 ####################
def fib(n):
    if n < 2: 
        return 1
    else:
        return fib(n-2) + fib(n-1)

def fib_proof(n):
    return fib(n) >= 2**(n/2) and fib(n) <= 2**n

# for value 1 the assertment still holds true because both powers resolve to 1
# for n = 0 and for value 1 the assertment is false because 2**(1/2) > 1 while
# fib(1) = 1.
###############################################


############### Problem 4 ####################

# Estimating the quantity
def altSumOfSquares(n):
    altSum = 0
    for q in range(n + 1):
        altSum += (((-1)**(q - 1)) * (q**2))
    print("altSumOfSquares(" + str(n) + ") produces " + str(int(altSum)) + ".", file=open("problem4output.txt", "a")) 

def fig28result(n):
    print("fig28result(" + str(n) + ") produces " + str(int((-1)**(n - 1) * n * (n + 1) / 2)) + ".", file=open("problem4output.txt", "a")) 

def formulaGuess1(n):
    """
    We begin by noticing that the numbers for fig28result(n) alternate when we increment the input.
    The numbers start positive so the power must be even.
    """
    print("formulaGuess1(" + str(n) + ") produces " + str(int((-1)**(n - 1))) + ".", file=open("problem4output.txt", "a"))

def formulaGuess2(n):
    """
    Now that we have our sign correct, we must get the correct value. We must notice that if the numbers
    were all positive, we would have a simple sum of numbers from 1 to n.
    """
    _sum = 0
    for i in range(1, n + 1):
        _sum += i
    print("formulaGuess2(" + str(n) + ") produces " + str(int((-1)**(n - 1) * _sum)) + ".", file=open("problem4output.txt", "a"))

def formulaGuess3(n):
    """
    However, we can get the sum of numbers from 1 to n easily by replacing _sum.
    This is the final formula.
    """
    print("formulaGuess3(" + str(n) + ") produces " + str(int((-1)**(n - 1) * n * (n + 1) / 2)) + ".", file=open("problem4output.txt", "a"))

##############################################


############## Problem 5 #####################
def OPR(penta_list, count=None):
    if count == None: 
        count = 0
    for i in range(len(penta_list)):
        if penta_list[i] < 0:
            penta_list[i-1] += penta_list[i]
            if i >= len(penta_list) - 1:
                penta_list[0] += penta_list[i]
            else:
                penta_list[i+1] += penta_list[i]
            penta_list[i] = -penta_list[i]
            try:
                penta_list, count = OPR(penta_list, count + 1)
            except RecursionError:
                print("Calculation unsuccessful after " + str(count) + " iterations.", file=open("problem5output.txt", "a"))
            break
    return penta_list, count

# Part b
# See assignment2.doc
###############################################


################# Problem 6 ###################
def depth(n):
    if n < 2:
        return 1
    if n % 2 == 1:
        return 1 + depth(3 * n + 1)
    else:
        return 1 + depth(n / 2)

def run_depth_till_100():
    for i in range(101):
        iterations = depth(i)
        if i == 0:
            print("For i = " + str(i) + " depth = " + str(iterations) + ".", file=open("problem6output.txt", "w"))
        else:
            print("For i = " + str(i) + " depth = " + str(iterations) + ".", file=open("problem6output.txt", "a"))
################################################


################ Problem 7 #####################
# See assignment2.doc
################################################


############### Problem 8 ######################
# See assignment2.doc
################################################


############### Problem 9 ######################
# See assignment2.doc
################################################


############### Problem 10 #####################
# Part a.)
def I_L_BinTree(BinTree, L=None, I=None):
    if I == None:
        I = 0
    if L == None:
        L = 0
    if not BinTree[1]: 
        return L + 1, I
    else:
        I += 1
        L, I = I_L_BinTree(BinTree[1], L, I)
        L, I = I_L_BinTree(BinTree[2], L, I)
        return L, I

# Part b.)
# See assignment2.doc

# Part c.)
# See assignment2.doc
################################################



############# Output Generation ################

# Problem 2
for i in range(10):
    if i == 0:   
        print("f(%d) == %6f and g(%d) == %6f and p(%d) == %r." %(i, f(i), i,
            g(i), i, p(i)), file=open("problem2output.txt", "w"))
    else:
        print("f(%d) == %6f and g(%d) == %6f and p(%d) == %r." %(i, f(i), i, g(i), i, p(i)), file=open("problem2output.txt", "a"))

# Problem 3
for i in range(0, 12):
    if i == 0:
        print("2**(%d/2) == %d <= fib(%d) == %d <= 2**(%d) == %d --- %r" %(i, 2**(i/2), i, fib(i), i, 2**(i), fib_proof(i)), file=open("problem3output.txt", "w"))
    else:
        print("2**(%d/2) == %d <= fib(%d) == %d <= 2**(%d) == %d --- %r" %(i,
            2**(i/2), i, fib(i), i, 2**(i), fib_proof(i)),
            file=open("problem3output.txt", "a"))

# Problem 4
open("problem4output.txt", "w").close()
for i in range(1, 11):
    altSumOfSquares(i)

print("", file=open("problem4output.txt", "a"))
for i in range(1, 11):
    fig28result(i)

print("", file=open("problem4output.txt", "a"))
for i in range(1, 11):
    formulaGuess1(i)

print("", file=open("problem4output.txt", "a"))
for i in range(1, 11):
    formulaGuess2(i)

print("", file=open("problem4output.txt", "a"))
for i in range(1, 11):
    formulaGuess3(i)



# Problem 5
print(file=open("problem5output.txt", "w"))
print("The resulting list and iterations from OPR([0, 0, 0, 0, 0]) is: " + str(OPR([0, 0, 0, 0, 0])), file=open("problem5output.txt", "a"))
OPR([1, 0, -1, 0, 0]) # Negative Sum produces RecursionError
print("The resulting list and iterations from OPR([1, 2, -3, -4, 5]) is: " + str(OPR([1, 2, -3, -4, 5])), file=open("problem5output.txt", "a"))
print("The resulting list and iterations from OPR([-10, 3, 5, -4, 7]) is: " + str(OPR([-10, 3, 5, -4, 7])), file=open("problem5output.txt", "a"))
OPR([-10, 3, 3, -4, 7]) # Negative Sum produces RecursionError

# Problem 6
run_depth_till_100()



# Problem 10
print(I_L_BinTree([1, [], []]), file=open("problem10output.txt", "w"))
print(I_L_BinTree([1, [2, [], []], [3, [], []]]), file=open("problem10output.txt", "a"))
print(I_L_BinTree([1, [2, [4, [], []], [5, [], []]], [3, [], []]]), file=open("problem10output.txt", "a"))
print(I_L_BinTree([1, [2, [3, [4, [], []], [5, [], []]], [6, [], []]], [7, [],
     []]]), file=open("problem10output.txt", "a"))
################################################