def funct(*pos, **keyword):
    pos_var = [i for i in pos]
    keyword_var = [i for i in keyword.values()]
    count = 0
    for var in pos_var:
        if var in keyword_var:
            count += 1
    return count


print(funct(1, 2, 3, 4, x=1, y=2, z=3, w=5))
