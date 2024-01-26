#Dominic Woodruff

import copy

#checks every possible move onto the space y,x
def getMoves(board, y, x):
    moves = [0, 0, 0, 0, 0, 0]
    if board[y][x] == 2 or board[y][x] == 1:
        return [0, 0, 0, 0, 0, 0]
    try:
        if (board[y][x-1] == 1 and board[y][x-2] == 1 and x-2 >= 0):
            moves[0] = 1
    except IndexError: 
        moves[0] = 0
    try:
        if (board[y-1][x-1] == 1 and board[y-2][x-2] == 1 and x-2 >= 0 and y-2 >= 0):
            moves[1] = 1
    except IndexError: 
        moves[1] = 0
    try:
        if (board[y-1][x] == 1 and board[y-2][x] == 1 and y-2 >= 0):
            moves[2] = 1
    except IndexError: 
        moves[2] = 0
    try:
        if (board[y][x+1] == 1 and board[y][x+2] == 1 and x+2 < 5):
            moves[3] = 1
    except IndexError: 
        moves[3] = 0
    try:
        if (board[y+1][x+1] == 1 and board[y+2][x+2] == 1 and x+2 < 5  and y+2 < 5):
            moves[4] = 1
    except IndexError: 
        moves[4] = 0
    try:
        if (board[y+1][x] == 1 and board[y+2][x] == 1 and y+2 < 5):
            moves[5] = 1
    except IndexError:
        moves[5] = 0
    return moves

#makes the move basesd on option
#option starts on the left and rotates clockwise
#Moves are also centered on the 0 (empty space), not the 1 (peg)
def move(boardOrig, option, y, x):
    board = boardOrig
    if not getOptions(board):
        return 1
    if board[y][x] == 0 or option in range(0,5):
        if(option == 0):
            board[y][x] = 1
            board[y][x-1] = 0
            board[y][x-2] = 0
        elif(option == 1):
            board[y][x] = 1
            board[y-1][x-1] = 0
            board[y-2][x-2] = 0
        elif(option == 2):
            board[y][x] = 1
            board[y-1][x] = 0
            board[y-2][x] = 0
        elif(option == 3):
            board[y][x] = 1
            board[y][x+1] = 0
            board[y][x+2] = 0
        elif(option == 4):
            board[y][x] = 1
            board[y+1][x+1] = 0
            board[y+2][x+2] = 0
        elif(option == 5):
            board[y][x] = 1
            board[y+1][x] = 0
            board[y+2][x] = 0
    else:
        return 1
    return board

#Finds all of the available moves by checking moves on every space
def getOptions(board):
    movementOptions = []
    for y in range(0, 5):
        for x in range(0, y+1):
            if board[y][x] == 0:
                tempMoves = getMoves(board, y, x)
                if 1 in tempMoves:
                    for index, val in enumerate(tempMoves):
                        if val == 1:
                            movementOptions.append([index, y, x])
    return movementOptions
    
#Recursive DFS to find a board with 0 moves left and one peg (one 1) left
def solver(board, path, movementOptions=None):
    if movementOptions is None:
        movementOptions = getOptions(board)
    if path is None:
        path = []
    if not movementOptions:
        return checkBoardState(board)
    for option in movementOptions:
        boardcopy = copy.deepcopy(board)
        new_board = move(boardcopy, option[0], option[1], option[2])
        if new_board != 1:
            path.append(option)
            if solver(new_board, path, getOptions(new_board)):
                return True
            path.pop()
    return False

#checks how many 1's are left
def checkBoardState(board):
    ones = 0
    for row in board:
        for item in row:
            if item == 1:
                ones += 1
    if ones == 1:
        printBoard(board)
    return ones == 1

#prints the board in a readable manner
def printBoard(board):
    for row in board:
        print(row)
    print("")

#makes a board, moveing the 0 to a different 1's place results in new solutions
def createBoard():
    board = [[1, 2, 2, 2, 2], [1, 1, 2, 2, 2], [1, 0, 1, 2, 2], [1, 1, 1, 1, 2], [1, 1, 1, 1, 1]]
    printBoard(board)
    return board

#starts the recursion and reverse engineers the final board using the path
def main():
    board = createBoard()
    path = []
    solver(board, path)
    board = createBoard()
    print(path)
    for option in path:
        printBoard(board)
        board = move(board, option[0], option[1], option[2])
    lastmove = path[len(path)-1]
    move(board, lastmove[0], lastmove[1], lastmove[2])
    printBoard(board)


main()
