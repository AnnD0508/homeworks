a = {'a': 1, 'b': 2, 'c': 3}
b = {'c': 3, 'd': 4, 'e': 5}
ab = a.copy()
ab.update(b)

for k in ab.keys():
    ab[k] = [a.setdefault(k), b.setdefault(k)]

print(ab)
