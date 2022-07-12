#N-Queens solver using branch and bound dfs, branch and bound bfs and heuristics

def safe_dfs(r, j):                                                             #methods to check Queen pos safety
    if cols[j] or fwdslash[r + j] or bkwdslash[r - j + num_queens - 1]:
        return False
    return True

def safeTwo(r, j):
    if cols[j] or row[r] or fwdslash[r + j] or bkwdslash[r - j + num_queens - 1]:   #used for BFS and Heuristics
        return False
    return True

def solve_dfs(board, r, cols, fwdslash, bkwdslash):
    if r >= num_queens:                                             #base case
        return True
    for j in range(num_queens):                                     #Place one Queen per row
        print("visited:", r, j)
        if safe_dfs(r,j):                                            #if safe place the queen and update the lists
            print("Queen Placed")
            board[r][j] = 'Q'
            cols[j] = True
            fwdslash[r + j] = True
            bkwdslash[r - j + num_queens - 1] = True
            if solve_dfs(board, r + 1, cols, fwdslash, bkwdslash):    #move on to next row if safe
                return True
            else:                                                     #else mark the cell as 0 and try again
                board[r][j] = 0
                cols[j] = False
                fwdslash[r + j] = False
                bkwdslash[r - j + num_queens - 1] = False
    return False

def solve_bfs(board, r, cols, fwdslash, bkwdslash, row):

    if r >= num_queens:
        return True
    for i in range(num_queens):                               #search the board in level order
        for j in range(num_queens):
            print("visited",i, j)
            if safeTwo(i, j):
                print("Queen Placed:", i, j)
                board[i][j] = 'Q'
                cols[j] = True
                row[i] = True                                  #unlike dfs, row conflict is checked here
                fwdslash[i + j] = True
                bkwdslash[i - j + num_queens - 1] = True

                if solve_bfs(board, i + 1, cols, fwdslash, bkwdslash, row):
                    return True
                else:
                    board[i][j] = 0
                    cols[j] = False
                    row[i] = False
                    fwdslash[i + j] = False
                    bkwdslash[i - j + num_queens - 1] = False

    return False

def solve_dfs_problem():
    if not solve_dfs(board, 0, cols, fwdslash, bkwdslash):
        print("Solution does not exist")
        return False

    print(board)
    return True

def solve_bfs_problem():
    if not solve_bfs(board, 0, cols, fwdslash, bkwdslash,row):
        print("Solution does not exist")
        return False

    print(board)
    return True

def openpositionsinrow(board, row, num_queens):
    openposition = []
    for i in range(num_queens):
        if safeTwo(row, i):
            openposition.append([row,i])
    #print(openposition)
    #openposition.pop(0)
    #print(openposition)
    return openposition

def openpositioninrowcount(board, row, num_queens):
    return num_queens

def solve_h2(board, row, cols, fwdslash, bkwdslash):
    return True


overall = True
while overall:
    num_queens=int(input("Enter the number of Queens: "))

    row = [False] * num_queens
    cols = [False] * num_queens
    fwdslash = [False] * (2 * num_queens - 1)
    bkwdslash = [False] * (2 * num_queens - 1)

    def create_board(num):
        board = []

        for n in range(num):
            board.append([0]*num)
        return board

    print(create_board(num_queens))
    board = create_board(num_queens)

    choice = True
    while choice:
        selection=int(input("Select your algorithm: \n1.) Breadth First Search \n2.) Depth First Search-Branch_and_Bound \n3.) Heuristic Search\n \nEnter '9' to change board size\nEnter '0' to end game\n \n"))

        if selection == 0:
            choice = False
            overall = False
        elif selection == 9:
            choice = False
            overall = True
        elif selection == 1:
            print("Running BFS\n")
            solve_bfs_problem()

            row = [False] * num_queens
            cols = [False] * num_queens
            fwdslash = [False] * (2 * num_queens - 1)
            bkwdslash = [False] * (2 * num_queens - 1)

        elif selection == 2:
            print("Running DFS-Branch_and_Bound\n")
            solve_dfs_problem()

            row = [False] * num_queens
            cols = [False] * num_queens
            fwdslash = [False] * (2 * num_queens - 1)
            bkwdslash = [False] * (2 * num_queens - 1)

        elif selection == 3:
            print("Running Heuristic\n")
            openpositionsinrow(board, row, num_queens)
            solve_h2()
        else:
            print("Invalid Selection\n")