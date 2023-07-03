# Reshaping
import numpy as np

# create an 1d array containing numbers from 1 to 6
a = np.arange(1,7)
print(a)

b = a.reshape((2,3))
print(b)

# To add a new axis
# An axis add one more value to either row or column, wherever it is added
c = a[np.newaxis, :]
print(c)
print(c.shape)