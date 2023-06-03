import numpy as np

x = np.random.randint(0,5,(3,3))
print(x)
#array([[0, 1, 1],
#       [1, 3, 4],
#       [3, 2, 3]])

print(x.flatten())
#array([0, 1, 1, 1, 3, 4, 3, 2, 3])

y = x.flatten()
print(y)
#array([0, 1, 1, 1, 3, 4, 3, 2, 3])

x[0,1]=12
print(y)
array([0, 1, 1, 1, 3, 4, 3, 2, 3])

z = np.ravel(x)
x[0,1]=12

print(z)
#array([ 0, 12,  1,  1,  3,  4,  3,  2,  3])

print(y.base is None)
#True
#Meaning that y is a copy of x, hence doesn't point to the 'x' array
print(z.base is None)
#False
#Meaning that z is a view of x, hence point to the 'x' array
