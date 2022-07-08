overall = True
while overall:
    num_queens=int(input("Enter the number of Queens: "))

    def create_board(num):
        board = []

        for n in range(num):
            board.append([0]*num)
        return board

    print(create_board(num_queens))

    choice = True
    while choice:
        selection=int(input("Select your algorithm: \n1.) Breadth First Search \n2.) Depth First Search \n3.) Heuristic Search\n \nEnter '0' to end game\n \n"))

        if selection == 0:
            choice = False
            overall = False
        elif selection == 1:
            print("Running BFS\n")
        elif selection == 2:
            print("Running DFS\n")
        elif selection == 3:
            print("Running Heuristic\n")
        else:
            print("Invalid Selection\n")
