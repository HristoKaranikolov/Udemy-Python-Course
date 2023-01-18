some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

all_duplicates = {}
for value in some_list:
    curr_value_count = some_list.count(value)
    if curr_value_count > 1:
        all_duplicates[value] = curr_value_count

print(all_duplicates)
