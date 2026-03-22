import numpy as np
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
c = np.array([4, 5, 6, 9])

x = np.dot(a, b)
print(np.dot(x, c))