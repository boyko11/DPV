
#numbers = [-2, 7, 1, -5, 8, -3, 10, -55, -7, 17]
#numbers = [-2, -7, -100, -1, -9]
numbers = [2, 7, 100, 1, 9]

max_sum = [numbers[0]]

for i in range(1, len(numbers)):
    max_sum.append(
        max(
            numbers[i],
            numbers[i] + max_sum[i - 1],
            max_sum[i - 1])
    );

print(max_sum)