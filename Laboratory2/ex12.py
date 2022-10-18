def group_by_rhyme(listt):
    sort_list = sorted(listt, key=lambda i: i[-2:])
    result = []
    while len(sort_list) > 0:
        index = 0
        temp = [sort_list[index]]
        while index+1 < len(sort_list) and sort_list[index][-2:] == sort_list[index+1][-2:]:
            temp.append(sort_list[index+1])
            sort_list.pop(index)
        sort_list.pop(index)
        result.append(temp)
    return result


l = ['ana', 'banana', 'carte', 'arme', 'parte']
print(group_by_rhyme(l))