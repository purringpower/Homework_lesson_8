orders = [
    [34587, 'Learning Python, Mark Lutz', 4, 40.95],
    [98762, 'Programming Python, Mark Lutz', 5, 56.80],
    [77226, 'Head First Python, Paul Barry', 3, 32.95],
    [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
]

short_list = []

for i in range(len(orders)):
    if orders[i][2] * orders[i][3] < 100:
        short_list.append((orders[i][0], orders[i][2] * orders[i][3] + 10))
    else:
        short_list.append((orders[i][0], orders[i][2] * orders[i][3]))

print(short_list)
