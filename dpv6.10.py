import numpy as np
np.set_printoptions(suppress=True)

k = 4
p_coins = [0, .5, .5, .5, .5]

prob = np.empty((k + 1, len(p_coins)), np.float32)

prob[:, 0] = 0
prob[0, 0] = 1
for j in range(1, len(p_coins)):
    prob[0, j] = prob[0, j - 1] * (1 - p_coins[j])

for i in range(1, k + 1):
    for j in range(1, len(p_coins)):
        prob[i, j] = \
            prob[i-1, j-1] * p_coins[j] + \
            prob[i, j-1] * (1 - p_coins[j])

print(prob)