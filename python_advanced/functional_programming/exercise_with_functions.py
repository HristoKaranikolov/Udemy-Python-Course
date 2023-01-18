from functools import reduce


# 1 Problem
def capitalize_items(item):
    return item.upper()


my_pets = ['sisi', 'bibi', 'titi', 'carla']
print(list(map(capitalize_items, my_pets)))

# 2 Problem
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]

print(list(zip(my_strings, sorted(my_numbers))))


# 3 Problem
def over_num50_filter(item):
    return item > 50


scores = [73, 20, 65, 19, 76, 100, 88]

print(list(filter(over_num50_filter, scores)))


# 4 Problem
def accumulate(acc, item):
    return acc + item


print(reduce(accumulate, (my_numbers + scores), 0))