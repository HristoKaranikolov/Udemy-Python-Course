def generator_function(num):
    for i in range(num):
        yield i


g = generator_function(100)
print(g)
