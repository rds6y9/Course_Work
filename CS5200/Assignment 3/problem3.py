#####################################
# Programmer:	Ryan Stoughton
# Class: 		CS 5200
# File: 		problem3.py
#####################################

def GCD(x, y):
	if x % y == 0:
		return y
	return GCD(y, x % y)

def find_d(num_list):
	if num_list == []:
		return []
	elif len(num_list) == 1:
		return num_list[0]
	else:
		number1 = num_list.pop(0)
		number2 = num_list.pop(0)
		num_list.insert(0, GCD(number1, number2))
		return find_d(num_list)


print(find_d([540051690381, 5404079462298, 3485942644184]))