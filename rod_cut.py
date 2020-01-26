
price = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
price = [0, 1, 5, 8, 9]
price = [0, 1, 5, 8, 9, 10, 17, 17, 20]

MP = [0]

breaks = [ -1 for i in range(len(price))]

for i in range(1, len(price)):
    MP.append(0)
    for j in range(i):
        j_profit = MP[j] + price[i - j]
        print(i, j, j_profit)
        if j_profit > MP[i]:
            MP[i] = j_profit
            breaks[i] = j
    print(MP[i], '------------------')

print(MP)
print(breaks)