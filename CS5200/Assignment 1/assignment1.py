##########################################################
# PROGRAMMER: Ryan Stoughton				 			 #
# PROFESSOR:  Dr. Markowsky                   			 #
# CLASS: 	  CS5200 - Analysis of Algorithms			 #
# FILE: 	  assignment1.py				 			 # 
# NOTE: 	  This file can be executed via command line #
#			  in order to rewrite output files.			 #
##########################################################

from time import time

# Problem 3
def altDif(num_list):
	"""
	Produces the alternating difference of numerical lists.
	Example: altDif([3 5 4]) = 3 - (5 - 4) = 3 - 1 = 2
	"""
	if not num_list:
		return []
	elif len(num_list) == 1:
		return num_list[0]
	else:
		return altDif(num_list[:-2] + [num_list[-2] - num_list[-1]])

# Problem 4
def f35q(n):
	"""
	This function determines what combination of 3's and 5's 
	is needed to make up any number greater than or equal to 8. 
	Example: 11 = 3 * 2 + 5 * 1
	"""
	if n < 8:
		return "Error"
	elif n % 5 == 0:
		return (0, int(n / 5))
	elif n % 5 == 1:
		return (2, int((n - 6) / 5))
	elif n % 5 == 2:
		return (4, int((n - 12) / 5))
	elif n % 5 == 3:
		return (1, int((n - 3) / 5))
	else:
		return (3, int((n - 9) / 5))

# Problem 5

# f(1) => 91
# f(-6) => 91
# f(200) => 190
# f(27) => 91


def myFunction(n):
	"""
	A rewrite of the original f() to be non-recursive.
	This version of the function is guaranteed to produce the 
	same results due to the fact that any number input that is
	less than 101 will increase to over 100, then oscillate until 
	the input to the function is 101.
	"""
	if n > 100:
		return n - 10
	else: 
		return 91


# Problem 6

# A(2, 2) => A(1, A(2, 1)) -
# A(2, 1) => A(1, A(2, 0)) -
# A(2, 0) => A(1, 1) -
# A(1, 1) => A(0, A(1, 0)) - 
# A(1, 0) => A(0, 1) -
# A(0, 1) => A(0, 2) -
# A(0, 2) => 3 -
# A(1, 3) => A(0, A(1, 2)) - 
# A(1, 2) => A(0, A(1, 1)) -
# A(1, 1) => A(0, A(1, 0)) -
# A(1, 0) => A(0, 1) -
# A(0, 1) => 2 -
# A(0, 2) => 3 -
# A(0, 3) => 4 -
# A(1, 4) => A(0, A(1, 3)) -
# A(1, 3) => A(0, A(1, 2)) -
# A(1, 2) => A(0, A(1, 1)) -
# A(1, 1) => A(0, A(1, 0)) -
# A(1, 0) => A(0, 1) -
# A(0, 1) => 2 -
# A(0, 2) => 3 -
# A(0, 3) => 4 -
# A(0, 4) => 5 - 
# A(0, 5) => 6 -
# A(0, 6) => 7 -


def A(x,y):
	"""Ackermann Function"""
	if x == 0: 
		return y+1
	elif y == 0:
		return A(x-1,1)
	else:
		return A(x-1,A(x,y-1))

# Produces recursion depth error at A(4, 4) on my machine (not the greatest).

# Problem 7 
def GCD2(a, b, x_1=1, y_1=0, x_2=0, y_2=1):
	"""
	a => 1st number to find GCD of 
	b => 2nd number to find GCD of
	x_1 => Initially represents the identity a = x_1 * a + 0 * b
	y_1 => Initially represents the identity a = 1 * a + y_1 * b
	x_2 => Initially represents the identity a = x_2 * a + 1 * b
	y_2 => Initially represents the identity a =  0 * a + y_2 * b
	x's and y's are not to be set initially by the user.
	"""
	if a % b == 0:
		return [b, x_2, y_2]
	else:
		g, s, t = GCD2(b, a % b, x_2, y_2, (x_1 - int(a / b) * x_2), (y_1 - int(a / b) * y_2))
		return [g, s, t] 

# Problem 8
def SuperReverse(_list, new_list=None):
	"""
	Takes a list of basic types and other lists and recursively reverses everything.
	Example: [1, 2, [1, 2, [1, 2, 3]]] => [[[3, 2, 1], 2, 1], 2, 1]
	"""

	# Needed to clear new_list on subsequent runs
	new_list = [] if new_list is None else new_list

	if _list == []:
		return new_list
	if type(_list[0]) == list:
		_list[0] = SuperReverse(_list[0])
	new_list.insert(0, _list.pop(0))
	return SuperReverse(_list, new_list)


# Problem 9
test_words = ['', 'a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh', 'abcdefghi', 'abcdefghij', 'abcdefghijk']

def myAnagram(word):
	"""Given a word, produces an anagram of the word in the form of a list."""
	if len(word) <= 1:
		return word
	current_permutations = []
	for permutation in myAnagram(word[1:]):
		for i in range(len(word)):
			current_permutations.append(permutation[:i] + word[0] + permutation[i:])
	# To make permutations unique
	return list(set(current_permutations))


def anagram(st):
	if st == '':
		return ['']
	lout = []
	for i in range(len(st)):
		st2 = st[:i] + st[i+1:]
		lout2 = anagram(st2)
		for w in lout2:
			lout.append(st[i]+w)
	return lout


def timeMyAnagram():
	for i in range(len(test_words)):
		start = time()
		myAnagram(test_words[i])
		end = time()
		print("Anagraming a word of length %d with myAnagram() took %fseconds!" %(i, end - start))

def timeOriginalAnagram():
	for i in range(len(test_words)):
		start = time()
		anagram(test_words[i])
		end = time()
		print("Anagraming a word of length %d with anagram() took %fseconds!" %(i, end - start))


# Execution of assignment1.py runs this to take input files
# and generate respective output files.

isFirstLine = True
with open('problem3input.txt') as f:
	for line in f:
		_list = list(map(int, line.split()))
		if isFirstLine:
			print("The result of altDif(" + str(_list) + ") was: " + str(altDif(_list)), file=open('problem3output.txt', 'w'))
			isFirstLine = False
		else:
			print("The result of altDif(" + str(_list) + ") was: " + str(altDif(_list)), file=open('problem3output.txt', 'a'))


isFirstLine = True
with open('problem4input.txt') as f:
	for line in f:
		_input = int(line)
		if isFirstLine:
			print("The result of f35q(" + str(_input) + ") was: " + str(f35q(_input)), file=open('problem4output.txt', 'w'))
			isFirstLine = False
		else:
			print("The result of f35q(" + str(_input) + ") was: " + str(f35q(_input)), file=open('problem4output.txt', 'a'))

isFirstLine = True
with open('problem5input.txt') as f:
	for line in f:
		_input = int(line)
		if isFirstLine:
			print("The result of myFunction(" + str(_input) + ") was: " + str(myFunction(_input)), file=open('problem5output.txt', 'w'))
			isFirstLine = False
		else:
			print("The result of myFunction(" + str(_input) + ") was: " + str(myFunction(_input)), file=open('problem5output.txt', 'a'))

isFirstLine = True
with open('problem6input.txt') as f:
	for line in f:
		_input = list(map(int, line.split()))
		if isFirstLine:
			print("The result of A(" + str(_input[0]) + ", " + str(_input[1]) + ") was: " + str(A(_input[0], _input[1])), file=open('problem6output.txt', 'w'))
			isFirstLine = False
		else:
			print("The result of A(" + str(_input[0]) + ", " + str(_input[1]) + ") was: " + str(A(_input[0], _input[1])), file=open('problem6output.txt', 'a'))

isFirstLine = True
with open('problem7input.txt') as f:
	for line in f:
		_input = list(map(int, line.split()))
		if isFirstLine:
			print("The result of GCD2(" + str(_input[0]) + ", " + str(_input[1]) + ") was: " + str(GCD2(_input[0], _input[1])), file=open('problem7output.txt', 'w'))
			isFirstLine = False
		else:
			print("The result of GCD2(" + str(_input[0]) + ", " + str(_input[1]) + ") was: " + str(GCD2(_input[0], _input[1])), file=open('problem7output.txt', 'a'))

isFirstLine = True
with open('problem8input.txt') as f:
	for line in f:
		_input = list(map(int, line.split()))
		if isFirstLine:
			print("The result of SuperReverse(" + str(_input) + ") was: " + str(SuperReverse(_input)), file=open('problem8output.txt', 'w'))
			isFirstLine = False
		else:
			print("The result of SuperReverse(" + str(_input) + ") was: " + str(SuperReverse(_input)), file=open('problem8output.txt', 'a'))

# I'm sorry, I cannot figure out how to input manually a list inside of a list. Here is a hand-coded test
	print("The result of SuperReverse(" + str([1, 2, 3, 4, [1, 2, [1, 2, 3], 3], 5]) + ") was: " + str(SuperReverse([1, 2, 3, 4, [1, 2, [1, 2, 3], 3], 5])), file=open('problem8output.txt', 'a'))

isFirstLine = True
with open('problem9input.txt') as f:
	for line in f:
		_input = str(line[:-1]) # To get rid of \n
		if isFirstLine:
			print("The result of myAnagram(" + _input + ") was: " + str(myAnagram(_input)), file=open('problem9output.txt', 'w'))
			isFirstLine = False
		else:
			print("The result of myAnagram(" + _input + ") was: " + str(myAnagram(_input)), file=open('problem9output.txt', 'a'))