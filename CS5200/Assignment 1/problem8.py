###############################################
# PROGRAMMER: Ryan Stoughton				  #
# PROFESSOR:  Dr. Markowsky                   #
# CLASS: 	  CS5200 - Analysis of Algorithms #
# FILE:		  problem8.py					  # 
###############################################


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
