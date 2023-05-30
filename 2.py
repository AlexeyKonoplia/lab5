def findElement(matrix, target):
    M, N = len(matrix), len(matrix[0])
    row, column = 0, N - 1

    while row < M and column >= 0:
        if matrix[row][column] == target:
            return row, column
        elif matrix[row][column] > target:
            column -= 1
        else:
            row += 1

    return -1

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
target = 9
print('Матрица', *matrix, sep = '\n')
print('Искомый элемент', target)
print('Результат', findElement(matrix, target))