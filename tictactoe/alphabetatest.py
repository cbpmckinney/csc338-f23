# Tic Tac Toe Project
# Uses PyGame Community Edition
# And Minimax/Alpha-beta pruning

import sys

numevals = 0


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







def GetBestMove(currentboard, turnsplayed):
    minscore = -sys.maxsize
    bestmove = None
    for i in GetPossibleMoves(currentboard):
        currentboard[i] = 2
        print("AI Considering move ", i , " at depth ", turnsplayed)
        PrintBoard(currentboard)
        score = MiniMax(currentboard, 2, turnsplayed + 1, -sys.maxsize, sys.maxsize)
        currentboard[i] = 0
        if score > minscore:
            minscore = score
            bestmove = i
    return bestmove  

def terminalmove(turnsplayed, alpha, beta, terminalvalue):
    print("Pausing at terminal node")
    print("(Alpha, beta, value) = ", alpha, beta, terminalvalue)
    input("Press any key to continue: ")


def GetPossibleMoves(currentboard):
    PossibleMoves = []
    for i in range(0,9):
        if currentboard[i] == 0:
            PossibleMoves.append(i)
    return PossibleMoves

def MiniMax(currentboard, playerturn, turnsplayed, alpha, beta):
    # returns a move and a score
    global numevals 
    numevals = numevals +1
    winner = CheckWin(currentboard)

    if winner == 1:
        terminalmove(turnsplayed, alpha, beta, turnsplayed-10)
        return turnsplayed-10
        
    elif winner == 2:
        terminalmove(turnsplayed, alpha, beta, 10-turnsplayed)
        return 10-turnsplayed
        
    elif winner == 3:
        terminalmove(turnsplayed, alpha, beta, 0)
        return 0


    if playerturn == 1:
        maxscore = -sys.maxsize
        for i in GetPossibleMoves(currentboard):
            print("Evaluating move as Max: ", i, " at depth ", turnsplayed)
            currentboard[i] = 2
            PrintBoard(currentboard)
            score = MiniMax(currentboard, 2, turnsplayed + 1, alpha, beta)
            currentboard[i] = 0
            maxscore = max(score, maxscore)
            alpha = max(alpha, maxscore)
            if maxscore >= beta:
                print("Breaking!  Maxscore, alpha, beta, depth: ", maxscore, alpha, beta, turnsplayed)
                break
        return maxscore
    else:
        minscore = sys.maxsize
        for i in GetPossibleMoves(currentboard):
            currentboard[i] = 1
            print("Evaluating move as Min: ", i, " at depth ", turnsplayed)
            PrintBoard(currentboard)
            score = MiniMax(currentboard,1, turnsplayed+1, alpha, beta)
            currentboard[i] = 0
            minscore = min(score, minscore)
            beta = min(beta, minscore)
            if minscore <= alpha:
                print("Breaking!  Minscore, alpha, beta, depth: ", minscore, alpha, beta, turnsplayed)
                break
        return minscore



#gameboard = [0] * 9
gameboard = [2,1,1,2,0,0,0,0,0]
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
        aimove = GetBestMove(gameboard, turns)
        print("AI Chooses: " + str(aimove))
        gameboard[aimove] = 2
        playerturn = 1
        turns = turns+1
    gamestate = CheckWin(gameboard)
    #print(gamestate)

if (gamestate == 1):
    print("Player wins!")
    PrintBoard(gameboard)
elif(gamestate == 2):
    print("AI wins!")
    PrintBoard(gameboard)
else:
    print("Stalemate!")
    PrintBoard(gameboard)

print("Number of evals: ", numevals)


