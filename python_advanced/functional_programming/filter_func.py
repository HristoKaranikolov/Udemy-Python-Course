def return_odd_nums(item):
    return not item % 2 == 0


my_list = [1, 2, 3, 4, 5, 6]
print(list(filter(return_odd_nums, my_list)))
print(my_list)