#####################################
# Programmer:	Ryan Stoughton
# Class: 		CS 5200
# File: 		problem2.py
#####################################


# GCD function from Chapter 2
def GCD(a, b):
	if a % b == 0:
		return b
	return GCD(b, a % b)

