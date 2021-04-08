orders = [
    [34587, 'Learning Python, Mark Lutz', 4, 40.95],
    [98762, 'Programming Python, Mark Lutz', 5, 56.80],
    [77226, 'Head First Python, Paul Barry', 3, 32.95],
    [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
]


def short_lists_maker(long_list):
    short_list = []
    for i in range(len(long_list)):
        if long_list[i][2] * long_list[i][3] < 100:
            short_list.append((long_list[i][0], long_list[i][2] * long_list[i][3] + 10))
        else:
            short_list.append((long_list[i][0], long_list[i][2] * long_list[i][3]))

    print(short_list)


short_lists_maker(orders)

