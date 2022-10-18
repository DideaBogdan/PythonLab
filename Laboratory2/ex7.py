def palindrome_tuple(l):
    pali_list = []
    for index in l:
        if str(index) == str(index)[::-1]:
            pali_list.append(index)
    maxi = max(pali_list)
    res = len(pali_list), maxi
    return res


llist = [1, 22, 12321, 578889, 56765]
print(palindrome_tuple(llist))
