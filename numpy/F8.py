# Generating arrays
import numpy as np

a = np.zeros((2,3))
print(a)

a = np.ones((2,3))
print(a)

a = np.full((2,3), 7.5)
print(a)

# identity matrix
a = np.eye(3)
print(a)

a = np.arange(20)
print(a)

# last parameter tells the number of elements the array should contain
# To create equally spaced arrays
a = np.linspace(0, 10, 5)
print(a)