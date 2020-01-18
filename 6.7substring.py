#Longest Palindromic Substring

import numpy as np

s = "hgtrfedactgtgtcaaaatcg"

L = np.zeros((len(s), len(s)), np.int)

for i in range(len(s)):
    L[i, i] = 1
    if i < len(s) - 1 and s[i] == s[i + 1]:
        L[i, i + 1] = 2

for l in range(3, len(s) + 1):
    for i in range(len(s) - l + 1):
        j = i + l - 1
        if s[i] == s[j] and L[i + 1, j - 1] == j - i - 2 + 1:
            L[i, j] = 2 + L[i + 1, j - 1]

print(L)
print(np.max(L))