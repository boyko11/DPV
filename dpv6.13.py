
nums = [1, 5, 233, 7]


max_score = [[0 for x in range(len(nums))] for i in range(len(nums))]
for i in range(len(nums)):
    max_score[i][i] = nums[i]

for l in range(1, len(nums)):
    for i in range(len(nums) - l):
        j = i + l
        max_score[i][j] = max(nums[i] - max_score[i + 1][j], nums[j] - max_score[i][j - 1])

print("Player 1 wins: ", max_score[0][-1] > 0)