import numpy as np
np.set_printoptions(suppress=True)

a_games_needed = 3
b_games_needed = 1

prob = np.empty((a_games_needed + 1, b_games_needed + 1), np.float32)

prob[:, 0] = 0
prob[0, :] = 1


for i in range(1, a_games_needed + 1):
    for j in range(1, b_games_needed + 1):
        prob[i, j] = 0.5 * prob[i-1, j] + 0.5 * prob[i, j - 1]


#print(prob)

print("Answer: A's probability to win: ", prob[a_games_needed, b_games_needed])