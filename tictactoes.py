def makeboard():
    board =[]
    for i in range(3):
        board.append(["-","-","-"])
    return board
    
board = makeboard()

def checkwin(boardstate, turnnum):
    win = ""
    # draw
    if turnnum == 9:
        win = "Draw!"
        return win
    # rows
    for i in range(3):
        symb = boardstate[i][0]
        if symb != "-":
            rowwin = all(symbol == symb for symbol in boardstate[i])
            if rowwin:
                win = symb + " Wins!"
                return win
    # columns
    for i in range(3):
        symb = boardstate[i][0]
        if symb != "-":
            columnwin = ((boardstate[1][i] == symb) and (boardstate[2][i] == symb))
            if columnwin:
                win = symb + " Wins!"
                return win
    # diagonals
    for i in range(2):
        symb = boardstate[0][2*i]
        if symb != "-":
            diagwin = ((boardstate[1][1] == symb) and (boardstate[2][2-2*i] == symb))
            if diagwin:
                win = symb + " Wins!"
                return win
    return win

def play():
    global board
    turnnum = 0
    turn = "" ; win = ""
    while turn.lower() != "x" and turn.lower() != "o":
        turn = input("Who plays first (X/O)? ")
    
    while win == "":
        for thing in board:
            print(thing)
        print(f"{turn.upper()} plays")
        while True:
            row = input("Row: ")
            column = input("Colum: ")
            try:
                movexy = board[int(row)-1][int(column)-1]
            except:
                print("invalid coordinates, try again")
            else:
                if movexy == "-":
                    board[int(row)-1][int(column)-1] = turn.upper()
                    if turn.lower() == "x":
                        turn = "O"
                    else:
                        turn = "X"
                    turnnum += 1
                    break
                else:
                    print("Square is occupied")
        win = checkwin(board, turnnum)
    for thing in board:
        print(thing)
    print(win)
                
        
play()