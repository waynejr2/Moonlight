N = 8
stateschecked=0

board = [[0 for i in range(N)] for j in range(N)]

rows = [False] * N
cols = [False] * N
fwdslash = [False] * (2 * N - 1)
bkwdslash = [False] * (2 * N - 1)


def openpositionsinrow(board, row, N):
    openposition = []
    for i in range(N):
        if safe(row, i):
            openposition.append([row,i])
    #print(openposition)
    #openposition.pop(0)
    #print(openposition)
    return openposition

def openpositioninrowcount(board, row, N):
    return N

def safe(row, j):
    if cols[j] or rows[row] or fwdslash[row + j] or bkwdslash[row - j + N - 1]:
        return False
    return True


def solve_h2(board, row, cols, fwdslash, bkwdslash):
    return True

def solutionH2():

    if not solve_h2(board, 0, cols, fwdslash, bkwdslash):
        print("Solution does not exist")
        return False

    print(board)
    return True


solutionH2()
openpositionsinrow(board, 0, 8)