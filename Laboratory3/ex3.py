def comp_dictionaries(first, second):
    temp_first = first.items()
    temp_second = second.items()
    temp_first = sorted(temp_first)
    temp_second = sorted(temp_second)
    if len(temp_second) != len(temp_first):
        return False
    for (value1, value2) in zip(temp_first, temp_second):
        x1, y1 = value1
        x2, y2 = value2
        if type(y1) != type(y2):
            return False
        if type(x1) != type(x2):
            return False
        if (type(y1) == dict and type(y2) == dict) or (type(y1) == set and type(y2) == set):
            comp_dictionaries(y1, y2)
        if (type(x1) == dict and type(x2) == dict) or (type(x1) == set and type(x2) == set):
            comp_dictionaries(x1, x2)
        if x1 != x2 or y1 != y2:
            return False
    return True


first_dict = dict(zip([chr(i) for i in range(ord("z"), ord("a")-1, -1)], [i for i in range(1, 27)]))
first_dict.setdefault("AA", {"AAA": 34})
second_dict = dict(zip([chr(i) for i in range(ord("z"), ord("a")-1, -1)], [i for i in range(1, 27)]))
second_dict.setdefault("AA", {"AAA": 44})
print(comp_dictionaries(first_dict, second_dict))