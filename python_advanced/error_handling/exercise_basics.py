while True:
    try:
        age = int(input('What is your age? - '))
        div = 10 / age
        print(div)
    except (ValueError, ZeroDivisionError) as val_er:
        print(f"Please enter a valid number! - {val_er}")
    else:
        print('Thank you!')
        break
    finally:
        pass


def summing(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:
        print(f'Please enter numbers! - {err}')


print(summing(1, '2'))
