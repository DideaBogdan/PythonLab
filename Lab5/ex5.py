def my_function(lst):
    res =[]
    for items in lst:
        if type(items) == int or type(items) == float or type(items) == complex:
            res.append(items)
    return res


print(my_function([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0, 5+3j]))
