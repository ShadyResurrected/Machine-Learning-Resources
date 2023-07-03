# Broadcasting

import numpy as np

x = np.array([[1,2,3],[4,5,6],[7,8,9]])
a = np.array([[1,0,1]])
y = x + a
print(y)

# copying
b = np.array([1,2,3])
# This will make a new instance rather than pointing to the same memory location as that of b
c = b.copy()
c[0] = 89
print(b)