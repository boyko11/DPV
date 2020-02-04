import numpy as np

s = [5, 7, 4, -3, 9, 1, 10, 4, 5, 8, 9, 3]
prev = [None for i in range(len(s))]

lis = [1]

for i in range(1, len(s)):
    lis.append(1)
    for j in range(i):
        if s[i] > s[j]:
            if lis[j] + 1 > lis[i]:
                prev[i] = j
                lis[i] = lis[j] + 1

print(lis)
print(prev)
max_index = np.argmax(lis)
prev_index = prev[max_index]
answer = [s[max_index]]

while prev_index is not None:
    answer.insert(0, s[prev_index])
    prev_index = prev[prev_index]

print(answer)





