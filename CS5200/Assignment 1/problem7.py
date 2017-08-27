###############################################
# PROGRAMMER: Ryan Stoughton				  #
# PROFESSOR:  Dr. Markowsky                   #
# CLASS: 	  CS5200 - Analysis of Algorithms #
# FILE:		  problem7.py					  # 
###############################################


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