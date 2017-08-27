###############################################
# PROGRAMMER: Ryan Stoughton				  #
# PROFESSOR:  Dr. Markowsky                   #
# CLASS: 	  CS5200 - Analysis of Algorithms #
# FILE:		  problem5.py					  # 
###############################################


# ORIGINAL FUNCTION
# def f(n):
# 	if n > 100:
# 		return n - 10;
# 	else: 
# 		return f(f(n + 11))


# f(1) => 91
# f(-6) => 91
# f(200) => 190
# f(27) => 91


def f(n):
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