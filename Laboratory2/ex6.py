def count_x(x, *list_of_lists):
    dict = {}
    for index in list_of_lists:
        for j in index:
            if j in dict:
                dict[j] += 1
            else:
                dict.setdefault(j, 1)
    #print(dict)
    res = [value for value in dict if dict[value] == x]
    return res
0

a = [1, 2, 3, 4, 5]
b = [1, 1, 9, 9, 6, 6, 8, 8, 5, 5, 5, 2]
x = 2
print(count_x(x, a, b))

