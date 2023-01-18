def highest_even(ls):
    highest_even_num = 0
    for num in ls:
        if num % 2 == 0 and num > highest_even_num:
            highest_even_num = num
    return highest_even_num


print(highest_even([10, 2, 3, 14, 5, 7, 8]))
