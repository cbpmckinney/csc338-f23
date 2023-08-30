# Tic Tac Toe Project
# Uses PyGame Community Edition
# And Minimax/Alpha-beta pruning

def CheckWin(currentboard):
# function should return 0 if no winner but also no draw
# return 1 if X wins
# return 2 if O wins
# return 3 if draw
    return 0

def PrintBoard(currentboard):
    print(currentboard[0:3])
    print(currentboard[3:6])
    print(currentboard[6:9])


gameboard = [0] * 9 
playerturn = 1 #1 is player 1, 2 is player 2
gamestate = 0 #0 for playing, 1 for 1 wins, 2 for 2 wins, 3 for draw
turnsplayed = 0

while(gamestate == 0):
    PrintBoard(gameboard)
    if(playerturn == 1):
        # Get player's input
        playermove = int(input("Choose a space 0 through 8: "))
        while(gameboard[playermove] != 0):
            playermove = input("Invalid move; choose again: ")
        gameboard[playermove] = 1
        playerturn = 2
        turnsplayed = turnsplayed+1
    else:
        #get AI's input
        aimove = minimax(gameboard, playerturn, turnsplayed)
        gameboard[aimove] = 2
        playerturn = 1
        turnsplayed = turnsplayed+1
    




