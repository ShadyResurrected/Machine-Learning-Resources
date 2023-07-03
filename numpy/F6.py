# Concatenation
import numpy as np

a = np.array([[1,2],[3,4]])
b = np.array([[5,6]])

# axis = None // converts it into a 1d array
# c = np.concatenate((a,b), axis=None)

# axis = 0 // joins it with the existing dimnesion of array
# c = np.concatenate((a,b), axis=0)

# axis = 1 // Joins one more column
c = np.concatenate((a,b.T), axis=1)
# print(c)

d = np.array([1,2,3,4])
e = np.array([5,6,7,8])
# hstack, vstack
f = np.hstack((d,e))
g = np.vstack((d,e))
print(f)
print(g)