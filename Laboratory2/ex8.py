def ascii_div(x, str_list, flag = True):
    result = []
    if flag:
        for index in str_list:
            temp_list = []
            for i in index:
                if ord(i) % x == 0:
                    temp_list.append(i)
            result.append(temp_list)
    else:
        for index in str_list:
            temp_list = []
            for i in index:
                if ord(i) % x != 0:
                    temp_list.append(i)
            result.append(temp_list)
    return result


x = 2
str = ["test", "hello", "lab002"]
flag = False
print("Ascii divides by x :", ascii_div(x, str))
print("Ascii does not divide by x :", ascii_div(x, str, flag))
