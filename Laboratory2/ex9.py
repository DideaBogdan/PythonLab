def cant_see(matrix):
    result = []
    for index in range(len(matrix)-1, -1, -1):
        for j in range(0,len(matrix[index]),1):
            for i in range(index-1, -1, -1):
                if matrix[index][j] <= matrix[i][j]:
                    result.append((index, j))
                    break
    print(result)


matrix = [[1, 2, 3, 2, 1, 1],
          [2, 4, 4, 3, 7, 2],
          [5, 5, 2, 5, 6, 4],
          [6, 6, 7, 6, 7, 5]]
cant_see(matrix)