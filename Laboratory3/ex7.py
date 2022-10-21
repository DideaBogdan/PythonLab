def create_op_dict(*list_of_sets):
    dictionary = {}
    for set1 in range(0, len(list_of_sets)-1):
        for set2 in range(set1+1, len(list_of_sets)):
            intersection = list_of_sets[set1].intersection(list_of_sets[set2])
            union = list_of_sets[set1].union(list_of_sets[set2])
            dif_ab = list_of_sets[set1].difference(list_of_sets[set2])
            dif_ba = list_of_sets[set1].difference(list_of_sets[set2])
            dictionary.setdefault(f'{list_of_sets[set1]} & {list_of_sets[set2]}', intersection)
            dictionary.setdefault(f'{list_of_sets[set1]} | {list_of_sets[set2]}', union)
            dictionary.setdefault(f'{list_of_sets[set1]} - {list_of_sets[set2]}', dif_ab)
            dictionary.setdefault(f'{list_of_sets[set2]} - {list_of_sets[set1]}', dif_ba)
            print("{")
            for key, value in dictionary.items():
                print("    \"", key, '\" : ', value)
            print("}")


s1 = {1, 2, 3}
s2 = {1, 2}
create_op_dict(s1, s2)
