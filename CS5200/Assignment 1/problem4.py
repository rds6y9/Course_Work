###############################################
# PROGRAMMER: Ryan Stoughton				  #
# PROFESSOR:  Dr. Markowsky                   #
# CLASS: 	  CS5200 - Analysis of Algorithms #
# FILE:		  problem4.py					  # 
###############################################


def f35q(n):
	"""
	This function determines what combination of 3's and 5's 
	is needed to make up any number greater than or equal to 8. 
	Example: 11 = 3 * 2 + 5 * 1
	"""
	if n < 8:
		return "Error"
	elif n % 5 == 0:
		return (0, int(n/5))
	elif n % 5 == 1:
		return (2, int((n - 6) / 5))
	elif n % 5 == 2:
		return (4, int((n - 12) / 5))
	elif n % 5 == 3:
		return (1, int((n - 3) / 5))
	else:
		return (3, int((n - 9) / 5))