def function(pairs):
    res = []
    for x, y in pairs:
        aux = dict()
        aux['sum'] = x + y
        aux['prod'] = x * y
        aux['pow'] = x ** y
        res.append(aux)
    return res


print(*function(pairs=[(5, 2), (19, 1), (30, 6), (2, 2)]), sep="\n")
