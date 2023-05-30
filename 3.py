def is_safe(board, row, col):
    for i in range(8):
        if board[row][i] == 1 or board[i][col] == 1:
            return False
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    i, j = row, col
    while i >= 0 and j < 8:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1
    return True
def solve_n_queens(board, row, count):
    if row == 8:
        count[0] += 1
        print_board(board)
        return
    for col in range(8):
        if is_safe(board, row, col):
            board[row][col] = 1
            solve_n_queens(board, row + 1, count)
            board[row][col] = 0 

def print_board(board):
    for i in range(8):
        for j in range(8):
            print(board[i][j], end=' ')
        print()
    print(' ')

board = [[0] * 8 for _ in range(8)]
count = [0]
solve_n_queens(board, 0, count)
print("Количество вариантов решения:", count[0])
