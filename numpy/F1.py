import numpy as np

a = np.array([1,2,3])
# a = np.array([[1,2,3],[4,5,6],[7,8,9]])

# It determines the dimension of the array
print(a.shape)
# prints the data type 
print(a.dtype)
# prints the number of dimension
print(a.ndim)
# prints the number of elements in the array
print(a.size)
# prints the size of each element present in the array
print(a.itemsize)

# Multiplication between two arrays
b = a * np.array([1,2,3])
print(b)