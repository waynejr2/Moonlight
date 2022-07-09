N = 4

board = [[0 for i in range(N)] for j in range(N)]

cols = [False] * N
fwdslash = [False] * (2 * N - 1)
bkwdslash = [False] * (2 * N - 1)


def safe(row, j):
    if cols[j] or fwdslash[row + j] or bkwdslash[row - j + N - 1]:
        return False
    return True

def solve_bfs(board, row, cols, fwdslash, bkwdslash):

    if row >= N:
        return True
    for j in range(N):
        print("visited:", row, j)
        if safe(row,j):
            board[row][j] = 'Q'
            cols[j] = True
            fwdslash[row + j] = True
            bkwdslash[row - j + N - 1] = True
            if solve_bfs(board, row + 1, cols, fwdslash, bkwdslash):
                return True
            else:
                board[row][j] = 0
                cols[j] = False
                fwdslash[row + j] = False
                bkwdslash[row - j + N - 1] = False
    return False

def solveproblem():

    if not solve_bfs(board, 0, cols, fwdslash, bkwdslash):
        print("Solution does not exist")
        return False

    print(board)
    return True

solveproblem()
