def makeboard3d():
    bigboard = []
    for i in range(3):
        board = []
        for i in range(3):
            board.append(["-","-","-"])
        bigboard.append(board)
    return bigboard

def checkwin(boardstate, turnnum):
    win = ""
    # draw
    if turnnum == 27:
        win = "Draw!"
        return win
    # FLAT
    for d in range(3):
        # rows
        for i in range(3):
            symb = boardstate[d][i][0]
            if symb != "-":
                rowwin = all(symbol == symb for symbol in boardstate[d][i])
                if rowwin:
                    win = symb + " Wins!"
                    return win
        # columns
        for i in range(3):
            symb = boardstate[d][i][0]
            if symb != "-":
                columnwin = ((boardstate[d][1][i] == symb) and (boardstate[d][2][i] == symb))
                if columnwin:
                    win = symb + " Wins!"
                    return win
        # diagonals
        for i in range(2):
            symb = boardstate[d][0][2*i]
            if symb != "-":
                diagwin = ((boardstate[d][1][1] == symb) and (boardstate[d][2][2-2*i] == symb))
                if diagwin:
                    win = symb + " Wins!"
                    return win
    # 3D
    # poles
    for i in range(3):
        for j in range(3):
            symb = boardstate[0][i][j]
            if symb != "-":
                polewin = ((boardstate[1][i][j] == symb) and (boardstate[2][i][j] == symb))
                if polewin:
                    win = symb + " Wins!"
                    return win
    # diaginals
    for i in range(2):
        for j in range(2):
            symb = boardstate[0][2*i][2*j]
            if symb != "-":
                ops = ["+","-"]
                diaginwin = (
                    ((boardstate[1][eval("i"+ops[i]+"1")][j] == symb) and (boardstate[2][eval("i"+ops[i]+"2")][j] == symb)) or
                    ((boardstate[1][i][eval("j"+ops[j]+"1")] == symb) and (boardstate[2][i][eval("j"+ops[j]+"2")] == symb))
                    )
                if diaginwin:
                    win = symb + " Wins!"
                    return win
    # diagoutals (and the center pole)
    for i in range(3):
        for j in range(3):
            symb = boardstate[0][i][j]
            if symb != "-":
                inv = [2,1,0]
                diagoutwin = ((boardstate[1][1][1] == symb) and (boardstate[2][inv[i]][inv[j]] == symb))
                if diagoutwin:
                    win = symb + " Wins!"
                    return win
    return win  

def play3d():
    global board
    turnnum = 0
    turn = "" ; win = ""
    while turn.lower() != "x" and turn.lower() != "o":
        turn = input("Who plays first (X/O)? ")
    turn = turn.upper()

    while win == "":
        for i in range(3):
            print(str(board[0][i]) + " " + str(board[1][i]) + " " + str(board[2][i]))
        print(f"{turn} plays")
        while True:
            depth = input("Depth: ")
            row = input("Row: ")
            column = input("Colum: ")
            try:
                movexy = board[int(depth)-1][int(row)-1][int(column)-1]
            except:
                print("invalid coordinates, try again")
            else:
                if movexy == "-":
                    board[int(depth)-1][int(row)-1][int(column)-1] = turn
                    if turn == "X":
                        turn = "O"
                    else:
                        turn = "X"
                    turnnum += 1
                    break
                else:
                    print("Square is occupied")
        win = checkwin(board, turnnum)
    for i in range(3):
        print(str(board[0][i]) + " " + str(board[1][i]) + " " + str(board[2][i]))
    print(win)

board = makeboard3d()          
play3d()
