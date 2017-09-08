####################################################
# Programmer: Ryan Stoughton
# Class: CS5200
# Assignment: 2
# File: assignment2.py
####################################################


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

def fib(n):
    if n < 2: 
        return 1
    else:
        return fib(n-2) + fib(n-1)

def fib_proof(n):
    return fib(n) >= 2**(n/2)

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
                print(str(count) + " at recursion error.")
            break
    return penta_list, count

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
    
for i in range(10):
    if i == 0:   
        print("f(%d) == %6f and g(%d) == %6f and p(%d) == %r." %(i, f(i), i,
            g(i), i, p(i)), file=open("problem2output.txt", "w"))
    else:
        print("f(%d) == %6f and g(%d) == %6f and p(%d) == %r." %(i, f(i), i, g(i), i, p(i)), file=open("problem2output.txt", "a"))

for i in range(0, 12):
    if i == 0:
        print("2**(%d/2) == %d <= fib(%d) == %d <= 2**(%d) == %d --- %r" %(i, 2**(i/2), i, fib(i), i, 2**(i), fib_proof(i)), file=open("problem3output.txt", "w"))
    else:
        print("2**(%d/2) == %d <= fib(%d) == %d <= 2**(%d) == %d --- %r" %(i,
            2**(i/2), i, fib(i), i, 2**(i), fib_proof(i)),
            file=open("problem3output.txt", "a"))

# for value 1 the assertment still holds true because both powers resolve to 1
# for n = 0 and for value 1 the assertment is false because 2**(1/2) > 1 while
# fib(1) = 1.

run_depth_till_100()

print(I_L_BinTree([1, [], []]))
print(I_L_BinTree([1, [2, [], []], [3, [], []]]))
print(I_L_BinTree([1, [2, [3, [4, [], []], [5, [], []]], [6, [], []]], [7, [],
    []]]))
