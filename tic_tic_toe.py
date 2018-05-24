#Tic Tac Toe
import random

def drawBoard(board):
    #This function prints out the board that it was passed
    print(board[7]+ "|" + board[8]+ '|'+ board[9])
    print('-+-+-')
    print(board[4]+ '|'+board[5]+ '|'+ board[6])
    print('-+-+-')
def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print("Do you want to be X or O ?")
        letter = input().upper()
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']
def whoGuesFirst():
    if random.randint(0,1) == 0:
        print("Computer will go first")
        return 'computer'
    else:
        print("Player will go first")
        return 'player'
def makeMove(board, letter, move):
    board[move] = letter
def getBoardCopy(board):
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy
def isSpaceFree(board, move):
    return board[move]

def getPlayerMove(board):
    #Let the player type in their move
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print("What is your next move? (1-9)" )
        move = input()
    return int(move)
def chooseRandomMoveFromList(board, movesList):
    #Returns a valid move from the passed list on the passed board
    #Returns None if there is no valid move
    possibleMoves = []
if __name__ == '__main__':
    whoGuesFirst()