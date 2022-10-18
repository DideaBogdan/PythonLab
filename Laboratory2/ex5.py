import numpy as np


def under_diag(matrix):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if i > j:
                matrix[i][j] = 0
    return matrix


numb = input("Enter number of rows and columns: ")
matrixx = np.random.randint(100, size=(int(numb), int(numb)))
print(matrixx)
print(under_diag(matrixx))
