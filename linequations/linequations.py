import numpy
from scipy import linalg

A = numpy.array([[6,4,1],
	[1,8,-2],
	[3,2,0]])
b = numpy.array([7,6,8])

Ainv = numpy.linalg.inv(A)

print(numpy.dot(Ainv, b))
print(numpy.linalg.solve(A,b))

lu = linalg.lu_factor(A)
print(linalg.lu_solve(lu,b))
