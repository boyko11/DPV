import numpy as np
np.set_printoptions(suppress=True)

X = [5, 10, 15]
V = 99

C = np.zeros(V + 1, np.int)

C[0] = 1 # we can make change for 0

for v in range(1, V + 1):
    for x in X:
        if x <= v and C[v] == 0:
            C[v] = 1 if C[v - x] == 1 else 0

print(C)
print(C[V])
