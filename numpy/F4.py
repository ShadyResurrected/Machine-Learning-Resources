# Indexing/Slicing/Boolean Indexing
import numpy as np

a = np.array([[1,2],[3,4]])

print(a.shape)

print(a[0,0])

# print all the first element from every row
print(a[:,0])

# Transpose the array
print(a.T)

# Inverse the array
print(np.linalg.inv(a))

# Determinant of the array
print(np.linalg.det(a))

# Diognal matrix
print(np.diag(a))

print(a[-1,-1])

# Evaluating boolean expressions

bool_idx = a > 1
print(bool_idx)

# Print only those elements where the result is evaluated to true (1d array)
print(a[bool_idx])

# Print the array elements where the value is greater than 1 else print -1
b = np.where(a>2, a, -1)
print(b)

# Fancy indexing
a = np.array([19,432,532,65,87,12,66,90,78,23])
print(a)
b = [1,3,5]
print(a[b])

# Print the even elements in the array
# flatten is used to convert it to 1d array
even = np.argwhere(a%2 == 0).flatten()
print(a[even])