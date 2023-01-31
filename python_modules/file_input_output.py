try:
    with open('./test.txt', mode='r') as my_file:
        print(my_file)
except FileNotFoundError as ex:
    print('Check your file path')
