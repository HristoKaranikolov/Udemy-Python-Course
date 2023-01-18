# Age guess program

found_age = False
age = 0
while not found_age:
    try:
        birth_year = int(input('What year were you born? - '))
        age = 2023 - birth_year
        found_age = True
    except ValueError:
        print('Oops, please write a number!')
        continue

print(f"You are a {age} years old.")
