from itertools import zip_longest


def sort_tuples(list):
    x = sorted(list, key = lambda i: i[1][2])
    return x

x = [('abc', 'bcd'), ('abc', 'zza')]
print(sort_tuples(x))
