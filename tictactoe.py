import sys
P1 = "X"
P2 = "O"


def new_board():
    new_board = list()
    for i in range(3):
        new_board.append(list())
        for _ in range(3):
            new_board[i].append(None)
    return new_board

def render(curr_board):
    brd = [x[:] for x in curr_board]
    print("    A  B  C")
    print("  -----------")
    for i in range(3):
        for j in range(3):
            if brd[i][j] == None:
                brd[i][j] = " "
        print("{} | {}  {}  {} |".format(str(i), brd[i][0], brd[i][1], brd[i][2]))
    print("  -----------")

def get_move():
    x = -1
    y = -1
    while x != 'A' and x != 'a' and x != 'b' and x != 'B' and x != 'C' and x != 'c':
        x = input("X: ")
    while y < 0 or y > 2:
        y = int(input("Y: "))
    if x == 'A' or x == 'a':
        x = 0
    elif x == 'B' or x == 'b':
        x = 1
    else:
        x = 2
    return (x,y)

def is_valid_move(curr_board, coords):
    x = coords[0]
    y = coords[1]
    if curr_board[y][x] == None:
        return True
    else:
        print("Invalid move!")
        return False

def make_move(curr_board, coords, player):
    brd = [x[:] for x in curr_board]
    x = coords[0]
    y = coords[1]
    brd[y][x] = player
    return brd

def get_state(curr_board):
    brd = [x[:] for x in curr_board]
    # Append diagonals
    brd.append([brd[0][0], brd[1][1], brd[2][2]])
    brd.append([brd[0][2], brd[1][1], brd[2][0]])
    # Append columns
    brd.append([brd[0][0], brd[1][0], brd[2][0]])
    brd.append([brd[0][1], brd[1][1], brd[2][1]])
    brd.append([brd[0][2], brd[1][2], brd[2][2]])
    
    check = 0
    for x in brd:
        if x[0] != None and x[0] == x[1] and x[1] == x[2]:
            print("Winner!")
            print(f"   {x[0]}")
            return True
        for y in x:
            if y == None:
                check = check + 1

    if check == 0:
        print("Draw!")
        return True
    return False


board = new_board()
render(board)
while True:
    coords = get_move()
    while not is_valid_move(board, coords):
        coords = get_move()
    board = make_move(board, coords, P1)
    render(board)
    if get_state(board):
        sys.exit(0)
    coords = get_move()
    while not is_valid_move(board, coords):
        coords = get_move()
    board = make_move(board, coords, P2)
    render(board)
    if get_state(board):
        sys.exit(0)