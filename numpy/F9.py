# Linear Algebra

import numpy as np

a = np.array([[1,2],[3,4]])
eignevalues, eigenvectors = np.linalg.eig(a)

print(eignevalues)
print(eigenvectors)  # column vector

# e_vec * e_val = A * e_vec

# Solving linear equations

# Method 1
A = np.array([[1,1], [1.5,4.0]])
b = np.array([2200,5050])

# X = A^-1 x b

x = np.linalg.inv(A).dot(b)
print(x)

# Method 2
x = np.linalg.solve(A, b)
print(x)