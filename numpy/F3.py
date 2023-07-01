import numpy as np

# dot product

l1 = [1,2,3]
l2 = [4,5,6]

dot = 0
for x in range(len(l1)):
    dot += l1[x] * l2[x]

print(f"Method 1: {dot}")

a1 = np.array(l1)
a2 = np.array(l2)

dot = np.dot(a1,a2)
print(f"Method 2: {dot}")

sum1 = a1 * a2
dot = np.sum(sum1)
print(f"Method 3: {dot}")

dot = a1 @ a2
print(f"Method 4: {dot}")