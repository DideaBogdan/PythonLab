def return_unique_and_duplicates(lista):
    return len(set(lista)), len(lista) - len(set(lista))


lista = [1, 1, 2, 3, 3, 4, 5, 5, 6]
print(return_unique_and_duplicates(lista))

