#####################################
# Programmer:	Ryan Stoughton
# Class: 		CS 5200
# File: 		problem1.py
#####################################

# Constants
# Note that C_VALUE must be greater than 10 for the 
# recursive function to halt. Therefore, iterative
# version has been written for values greater than 10
# to match the original.
C_VALUE = 11

# Original Function
def f(n):
	c = C_VALUE
	if n > 100: 
		return n - 10
	else: 
		return f(f(n + c))

# My Function
def fprime(n):
	c = C_VALUE
	count = 1
	while n < 100:
		n += c
		count += 1
	while count > 0:
		if n > 100:
			n -= 10
			count -= 1
		else:
			n += c
			count += 1
	return n

# Testing 
allAnswersAgree = True;
for i in range(10):
	for j in range(11, 100):
		C_VALUE = j
		answer1 = f(i)
		answer2 = fprime(i)
		print("With C_VALUE = " + str(j))
		print("f(" + str(i) + "): " + str(answer1))
		print("fprime(" + str(i) + "): " + str(answer2))
		if answer1 != answer2:
			allAnswersAgree = False
			break

print("All Answers Agree: " + str(allAnswersAgree))