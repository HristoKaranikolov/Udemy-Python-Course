from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'It took {t2 - t1} ms time')
        return result

    return wrapper


@performance
def long_time():
    a = 0
    for i in range(10000000):
        a = i * 5
        print(a)
    return a


long_time()
