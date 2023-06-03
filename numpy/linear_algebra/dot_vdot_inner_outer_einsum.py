import numpy as np

a = [[1, 2], [3, 1]]
b = [[4, 1], [2, 2]]

print(np.dot(a, b))
# [[1,2],  * [[4,1],
#  [3,1]]     [2,2]]
# [[1*4+2*2, 1*1+2*2],
#  [3*4+1*2, 3*1+2*1]]
#array([[4, 1],
#       [2, 2]])
# Note: for 2D array it's better to use np.matmul

np.dot([1+2j,3+4j],[5+6j,7+8j])
#(5+6j+10j-12+21+24j+28j-32)
#(-18+68j)


from numpy.linalg import multi_dot

# Prepare some data
A = np.random.random((10000, 100))
B = np.random.random((100, 1000))
C = np.random.random((1000, 5))
D = np.random.random((5, 333))
# the actual dot multiplication
_ = multi_dot([A, B, C, D])

#vdot stands for vectordot
#The vdot(a, b) function handles complex numbers differently 
# than dot(a, b). If the first argument is complex the complex
# conjugate of the first argument is used for the calculation of the dot product.

a = np.array([1+2j,3+4j])
b = np.array([5+6j,7+8j])
np.vdot(a, b)
#(70-8j)

#Same than earlier but use the conjugate as first argument, a=[1-2j,3-j]
np.vdot(b, a)
#(70+8j)

#np.inner(a, b) = sum(a[:]*b[:])
a = np.array([1,2,3])
b = np.array([1,1,4])
print(np.inner(a,b))
#15

#More generally, if ndim(a) = r > 0 and ndim(b) = s > 0:
#np.inner(a, b) = np.tensordot(a, b, axes=(-1,-1))