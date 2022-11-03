def pair(l):
    odd = [i for i in l if i % 2 == 1]
    even = [i for i in l if i % 2 == 0]
    res = [i for i in zip(even, odd)]
    print(res)

pair([1, 3, 5, 2, 8, 7, 4, 10, 9, 2])