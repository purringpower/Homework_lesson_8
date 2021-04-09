list_of_100 = [x for x in range(100)]
print(list(filter(lambda x: x % 3 == 0, list_of_100)))

print(list(map(lambda x, y: x ** y, [5, 6, 7, 8], [1, 2, 3, 4])))