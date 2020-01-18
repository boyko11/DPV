import numpy as np
np.set_printoptions(suppress=True)

numbers = [0, 3, 5, 7]
amount = 17

able_to_sum_up = np.zeros((len(numbers), amount + 1), np.int)

able_to_sum_up[0, :] = 0
able_to_sum_up[:, 0] = 1


for i in range(1, len(numbers)):
    for j in range(1, amount + 1):
        able_to_sum_up[i, j] = able_to_sum_up[i - 1, j] or \
                         (numbers[i] <= j and able_to_sum_up[i - 1, j - numbers[i]])

print(able_to_sum_up)
print("We can make change: ", able_to_sum_up[-1][-1])