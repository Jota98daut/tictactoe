import sys


def new_board():
    board = list()
    for i in range(3):
        board.append(list())
        for j in range(3):
            board[i].append(None)
    return board

def render(board):
    print("    A  B  C")
    print("  -----------")
    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                board[i][j] = " "
        print(str(i) + " | ", end='')
        print(str(board[i][0]) + '  ' + 
              str(board[i][1]) + '  ' + 
              str(board[i][2]), end='')
        print(" |")
    print("  -----------")

def get_move():
    x = "-1"
    y = "-1"
    while not x == 'A' and not x == 'a' and not x == 'B' and not x == 'b' and not x == 'C' and not x == 'c':
        x = input("X: ")
    while not int(y) >= 0 or not int(y) < 3:
        y = input("Y: ")
    return (x,y)

def make_move(board, player):
    coords = get_move()
    x = coords[0]
    y = coords[1]
    corY = int(y)
    if x == 'A' or x == 'a':
        corX = 0
    elif x == 'B' or x == 'b':
        corX = 1
    else:
        corX = 2
    if player == 1:
        board[corY][corX] = "X"
    else:
        board[corY][corX] = "O"
    return board

board = new_board()
render(board)
while True:
    board = make_move(board, 1)
    render(board)
    board = make_move(board, 2)
    render(board)