from collections import defaultdict, Counter, OrderedDict

li = [1, 2, 3, 6, 4, 5, 8, 6, 9, 7, 8]
print(Counter(li))


dictionary = defaultdict(lambda: 5, {'a': 1, 'b': 2})
print(dictionary['c'])

d = OrderedDict()
d['a'] = 1
d['b'] = 2


