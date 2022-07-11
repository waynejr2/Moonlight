N = 8
stateschecked=0

board = [[0 for i in range(N)] for j in range(N)]

rows = [False] * N
cols = [False] * N
fwdslash = [False] * (2 * N - 1)
bkwdslash = [False] * (2 * N - 1)

#Concept:  starting at the top row, you check each position.
#  you have to set position as if it is played, set statecount+1
#    then you have to check all following rows for the following:
#      the count of open squares on each row.  return the number which is the lowest count. 0 means it won't work
#      unset that postion and continue
#    after you have got the count for each of the moves, sorted from 0 and up.  Take the lowest non-zero and actually
#    play it.  repeat the above loop, until solved. you will likely have to go through the different options played as you go.
#    you will reach a solution if it exists.
#    Statecount should be near N.
#
#
#


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