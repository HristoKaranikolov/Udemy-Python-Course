class MyGen:
    current_iter = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if MyGen.current_iter < self.last:
            num = MyGen.current_iter
            MyGen.current_iter += 1
            return num
        raise StopIteration


generator = MyGen(0, 10)

for i in generator:
    print(i)
