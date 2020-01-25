import numpy as np
np.set_printoptions(suppress=True)

# X = "abdbabfgd"
# Y = "betfdbfafr"
# X = "abcertyerhx"
# Y = "aeritwojbpcaxeyerkhkjhx"
X = "abcdef"

Y = "bcdeabc"

L = np.zeros((len(X) + 1, len(Y) + 1), np.int16)

L[0, :] = 0  # the empty string will have zero in common
L[:, 0] = 0
for i in range(len(X)):
    l_i = i + 1
    for j in range(len(Y)):
        l_j = j + 1
        if X[i] == Y[j]:
            L[l_i, l_j] = L[l_i - 1, l_j - 1] + 1
        else:
            L[l_i, l_j] = L[l_i, l_j - 1]

print(L)