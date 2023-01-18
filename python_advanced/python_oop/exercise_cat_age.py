class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


def get_oldest_cat(cat_list):
    return max(cat_list)


jessica = Cat('Jessica', 5)
michael = Cat('Michael', 8)
tom = Cat('Tom', 2)

cats_ages = [jessica.age, michael.age, tom.age]
oldest_cat_age = get_oldest_cat(cats_ages)
print(f"The oldest cat is {oldest_cat_age} years old.")
