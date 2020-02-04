
a = [8, 2, 3, 5, 8, 7, 5, 3, 3, 3, 4]

min_a = min(a)
max_a = max(a)

count_a = [0 for i in range(max_a - min_a + 1)]

for i in range(len(a)):
    count_a_index = a[i] - min_a
    count_a[ count_a_index ] = count_a[ count_a_index ] + 1

print(count_a)

sorted_a = []
count_a_index = 0
for count in count_a:
    for i in range(count):
        sorted_a.append(count_a_index + min_a)
    count_a_index += 1

print(sorted_a)

