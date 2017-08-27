###############################################
# PROGRAMMER: Ryan Stoughton				  #
# PROFESSOR:  Dr. Markowsky                   #
# CLASS: 	  CS5200 - Analysis of Algorithms #
# FILE: 	  problem3.py					  # 
###############################################


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