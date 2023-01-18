picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]

]

for row_idx, row in enumerate(picture):
    for col in range(len(picture) + 1):
        curr_el = picture[row_idx][col]

        if curr_el == 0:
            
            picture[row_idx][col] = ' '
        else:
            picture[row_idx][col] = '*'

    print(''.join([str(x) for x in row]))

# for row in picture:
#     for pixel in row:
#         if pixel == 1:
#             print('*',end='')
#         else:
#             print(' ',end='')
#     print('')
