def list_op(n, m):
    x = [int(i) for i in n]
    y = [int(j) for j in m]
    intersection = [value for value in x if value in y]
    reunion = x + [value for value in y if value not in x]
    diff_ab = [value for value in x if value not in y]
    diff_ba = [value for value in y if value not in x]
    print(intersection)
    print(reunion)
    print(diff_ab)
    print(diff_ba)


numb1 = input("Insert  list of numbers: ").split()
numb2 = input("Insert  list of numbers: ").split()
list_op(numb1, numb2)
