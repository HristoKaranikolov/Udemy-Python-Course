# multiply py 2
my_list = [1, 2, 3]

print(list(map(lambda item: item * 2, my_list)))
print(my_list)

# Square
my_list = [5, 4, 3]

print(list(map(lambda a: a ** 2, my_list)))

# List sorting

ls = [(0, 2), (4, 3), (9, 9), (10, -1)]
ls.sort(key=lambda x: x[1])
print(ls)
