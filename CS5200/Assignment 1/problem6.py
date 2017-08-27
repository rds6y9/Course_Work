###############################################
# PROGRAMMER: Ryan Stoughton				  #
# PROFESSOR:  Dr. Markowsky                   #
# CLASS: 	  CS5200 - Analysis of Algorithms #
# FILE:		  problem6.py					  # 
###############################################

# Trace of A(2, 2) by hand (not fun)
# - means that the function line has been completely called.

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