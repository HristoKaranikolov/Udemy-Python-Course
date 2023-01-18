# List

print([num for num in range(0, 100)])
print([x for x in 'Helloo'])
print([num ** 2 for num in range(0, 100)])
print([num ** 2 for num in range(0, 100) if num % 2 == 0])
# ----------------------

# Dict
simple_dict = {"a": 2, 'b': 4, }
print({k: v ** 2 for k, v in simple_dict.items()})

print({num: num ** 2 for num in [1, 2, 3]})

# --------------
# Set

print({num for num in range(0, 100)})
print({x for x in 'Helloo'})
print({num ** 2 for num in range(0, 100)})
print({num ** 2 for num in range(0, 100) if num % 2 == 0})
