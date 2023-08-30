# Tic Tac Toe Project
# Uses PyGame Community Edition
# And Minimax/Alpha-beta pruning

import sys


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





def MiniMax(currentboard, playerturn, turnsplayed):
    # returns a move and a score
    bestmove = None
    
    tempboard = currentboard
    winner = CheckWin(tempboard)
    if winner == 1:
        return (None, turnsplayed - 10)
    elif winner == 2:
        return (None, 10 - turnsplayed)
    elif winner == 3:
        return (None, 0)
    
    if playerturn == 1:
        maxscore = -sys.maxsize
        bestmove = None
        for possiblemove in GetPossibleMoves(tempboard):
            tempboard[possiblemove] = 1
            (bestmove, score) = MiniMax(tempboard, 2, turnsplayed+1)
            tempboard[possiblemove] = 0
            if score > maxscore:
                maxscore = score
                bestmove = possiblemove
        return (bestmove, maxscore)

    else:
        minscore = sys.maxsize
        bestmove = None
        for possiblemove in GetPossibleMoves(tempboard):
            tempboard[possiblemove] = 2
            (bestmove, score) = MiniMax(tempboard, 1, turnsplayed+1)
            tempboard[possiblemove] = 0
            if score < minscore:
                minscore = score
                bestmove = possiblemove
        return (bestmove, minscore)


def GetPossibleMoves(currentboard):
    PossibleMoves = []
    for i in range(0,9):
        if currentboard[i] == 0:
            PossibleMoves.append(i)
    return PossibleMoves





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
        (aimove, score) = MiniMax(gameboard, playerturn, turnsplayed)
        print(aimove)
        gameboard[aimove] = 2
        playerturn = 1
        turnsplayed = turnsplayed+1
    gamestate = CheckWin(gameboard)
    print(gamestate)




