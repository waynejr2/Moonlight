# Python3 program to solve N Queen
# Problem using backtracking
global N
N = 4
result = []

def printSolution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()


# A utility function to check if a queen can
# be placed on board[row][col]. Note that this
# function is called when "col" queens are
# already placed in columns from 0 to col -1.
# So we need to check only left side for
# attacking queens
def isSafe(board, row, col):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Checks upper diagonal on right side
    for i, j in zip(range(row, -1, -1),
                    range(col, N, 1)):
        if board[i][j] == 1:
            return False

    # Checks lower diagonal on right side
    for i, j in zip(range(row, N, 1),
                    range(col, N, 1)):
        if board[i][j] == 1:
            return False

    return True

def DFS(board, col):
    if col >= N:
        return True

    else:
        for r in range(N):
            if isSafe(board, r, col):
                board[r][col] = 1
                if DFS(board, col+1) == True:
                    return True
                board[r][col] = 0

    return False

def solveNQ():
    board = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]

    DFS(board, 0)
    printSolution(board)
    return True


# Driver Code
solveNQ()