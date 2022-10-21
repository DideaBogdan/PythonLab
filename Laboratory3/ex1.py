def list_op(a, b):
    intersection = set(set(a) & set(b))
    reunion = set(set(a) | set(b))
    dif_ab = set(set(a) - set(b))
    dif_ba = set(set(b) - set(a))
    result = [intersection, reunion, dif_ab, dif_ba]
    print(result)


first = [1, 2, 3, 4, 5, 6]
second = [4, 5, 6, 7, 8, 9]
list_op(first, second)
