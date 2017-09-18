#####################################
# Programmer:	Ryan Stoughton
# Class: 		CS 5200
# File: 		problem4.py
#####################################

def sumOfAlternatingCubes(n):
	_sum = 0
	for i in range(1, n + 1):
		_sum += (((-1)**(i - 1)) * (i**3))
	return _sum

def g(n):
	return (((-1)**(n - 1)) * (n**3))

def h(n):
	return (g(n) / 2)

for n in range(1, 10):
	print("n: %3d   altCubes(n): %15.3f   g(n): %15.3f   ratio: %15.3f" % (n, sumOfAlternatingCubes(n), g(n), (sumOfAlternatingCubes(n)/g(n))))

for n in range(1, 10):
	print("n: %3d   altCubes(n): %15.3f   h(n): %15.3f   ratio: %15.3f" % (n, sumOfAlternatingCubes(n), h(n), (sumOfAlternatingCubes(n)/h(n))))

