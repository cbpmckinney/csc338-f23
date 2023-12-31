# Tic Tac Toe Project
# Uses PyGame Community Edition
# And Minimax/Alpha-beta pruning

import sys




#method for check win in AI Tic-Tac-Toe Game

#list to store winning possibilities in Tic-Tac-Toe Game
winning_index_combinations = ['048', '246', '147', '345', '036', '258', '012', '678']

def CheckWin(current_board):
    incomplete_board_check = False    
    #loop through winning combinations
    for combination in winning_index_combinations:
        #temp set int of winning combinations values for indexes
        index_integer_set = set()
        for index_character in combination:
            temp_index_int = int(index_character)
            if current_board[temp_index_int] == 0 : 
                incomplete_board_check = True
            index_integer_set.add(current_board[temp_index_int])
        
        #X(1) and O (2) winning check
        if len(index_integer_set) == 1:
            if 1 in index_integer_set:
                return 1
            if 2 in index_integer_set:
                return 2
            if 0 not in index_integer_set:
                print("Something Went Wrong")
    
    #draw or ongoing board check
    if incomplete_board_check :
        return 0
    else:
        return 3




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
                #print(bestmove, maxscore)
        #print(bestmove, maxscore)
        return (bestmove, maxscore)

    elif playerturn == 2:
        minscore = sys.maxsize
        bestmove = None
        for possiblemove in GetPossibleMoves(tempboard):
            tempboard[possiblemove] = 2
            (bestmove, score) = MiniMax(tempboard, 1, turnsplayed+1)
            tempboard[possiblemove] = 0
            print(minscore)
            if score < minscore:
                minscore = score
                bestmove = possiblemove
        #print(bestmove, minscore)
        return (bestmove, minscore)


def GetPossibleMoves(currentboard):
    PossibleMoves = []
    for i in range(0,9):
        if currentboard[i] == 0:
            PossibleMoves.append(i)
    return PossibleMoves





gameboard = [1,1,0,2,2,0,0,2,0]
playerturn = 1 #1 is player 1, 2 is player 2
gamestate = 0 #0 for playing, 1 for 1 wins, 2 for 2 wins, 3 for draw
turns = 0




while(gamestate == 0):
    PrintBoard(gameboard)
    if(playerturn == 1):
        # Get player's input
        playermove = int(input("Choose a space 0 through 8: "))
        while(gameboard[playermove] != 0):
            playermove = int(input("Invalid move; choose again: "))
        gameboard[playermove] = 1
        playerturn = 2
        turns = turns+1
    else:
        #get AI's input
        minscore = sys.maxsize
        for i in GetPossibleMoves(gameboard):
            gameboard[i] = 2
            (aimove, score) = MiniMax(gameboard, playerturn, 0)
            gameboard[i] = 0
            if score < minscore:
                bestscore = score
                bestmove = i 

        print(bestmove, score)
        print("AI Chooses: " + str(bestmove))
        gameboard[bestmove] = 2
        playerturn = 1
        turns = turns+1
    gamestate = CheckWin(gameboard)
    #print(gamestate)




