from itertools import zip_longest


def ret_tuples(*list_of_lists):
    tupl = zip_longest(*list_of_lists, fillvalue=None)
    return list(tupl)


x = [1, 2, 3]
y = [5, 6, 7]
z = ["a", "b", "c", "d"]
print(ret_tuples(x, y, z))
