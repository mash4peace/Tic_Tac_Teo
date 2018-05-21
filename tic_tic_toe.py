#This is tic tac toa game, normally playes with two people.
#One player is X and the other player is O.
#Players take turns placing their X and O.
#If a plater gerts three of their marks on the board in a row ,
#  column , or diagonal, they win, When the fills up  with neither player winning,
#  the game ends in a draw
import random
def drawBoard(board):
    #This function prints out the board that it was passed.
    #'board' is a list of 10 strings represents the board (ignore index 0)
    print(board[7] + '|' + board[8] + "|" + board[9])
    print("-+-+")
    print(board[4] + '|' + board[5] + "|" + board[6])
    print("-+-+")
    print(board[1] + '|' + board[2] + "|" + board[3])
def inputPlayerLetter():
    #Let the user type which letter they want to be
    #Returns a list with the player's letter  as the first item and
    #computer's letter as the second .
    letter = ''
    while not (letter == "X" or letter == "O"):
        print("Do you want to be X or O")
        letter = input().upper()
        # The first element in the list is the player's letter; the second is the computer's letter.
        if letter == "X":
            return ["X", "O"]
        else:
            return ["O", "X"]
def whoGuessFirst():
    #Randomly choose which player goes first
    if random.randint(0,1) == 0:
        return 'computer'
    else:
        return 'player'
def makeMove(board, letter, move):
    board[move]= letter
def isWinner(bo, le):
    #Give a board and a player's letter , this function returns True if the player won.
    #We use 'bo' to stand for board and le for letter
    return ((bo[7] == le and bo[8] == le, bo[9] == le ) or # Acros the top
            (bo[4] == le and bo[5] == le, bo[6] == le ) or #Across the middle.
            (bo[1] == le and bo[2] == le, bo[3] == le) or #Across the botton
            (bo[7] == le and bo[4] == le, bo[1] == le ) or #Down left side
            (bo[8] == le and bo[5] == le, bo[2] == le) or #Down middle side
            (bo[9] == le and bo[6] == le, bo[3] == le) or #Down the right
            (bo[7] == le and bo[5] == le, bo[3] == le) or #Diagnol
            (bo[9] == le and bo[5] == le, bo[1] == le))  #Diagnol
def getBoardCopy(board):
    #Make a copy of the board list and return it.
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy
def isSpaceFree(board, move):
    #Return True if the passes move is free on the pass board.
    return board[move] == ' '
def getPlayerMove(board):
    #Let the player enter their move
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print("What is your next move? (1-9)")
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, movelist):
    #Returns a valid from the passed list on the passed board

    #Returns None if there is no valid move
    possibleMoves = []
    for i in movelist:
         if isSpaceFree(board, i):
             possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLeter):
    #Given a board and the computer's letter , determine where to move and return that move
    if computerLeter == "X":
        playerLetter = 'O'

    else:
        playerLetter = 'X'

    #Here is the algorithm for our Tic- Tac- Toe AI:
    #First, check if we can win in the next move
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLeter, i)
            if isWinner(boardCopy, computerLeter):
                return i
    #Check if the player could win on their next move and block them.
    for i in range(1,10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, playerLetter):
                return i
    #Try to take one of the corner , if they are free
    move = chooseRandomMoveFromList(board,[1,3,7,9])
    if move != None:
        return move

    #Try to take the center , if it is free
    if isSpaceFree(board, 5):
        return 5
    #Move on one of the sides
    return chooseRandomMoveFromList(board, [2,4,6,8])

def isBoardFull(board):
    #Return True if every space on the board has been taken . Otherwise return False
    for i in range(1,10):
        if isSpaceFree(board, i):
            return False

    return True
print("Welcome to Tic-Tac-Toe")

while True:
    #Reset the board
    theBoard = [' ']*10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGuessFirst()
    print("The "+ turn + ' will go first.')
    gameIsPlaying = True
    while gameIsPlaying:
        if turn == 'player':
            #players turn
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print("Hooray! You have won the game!")
                gameIsPlaying = False

            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print("The game is a tie!")
                else:
                    turn = 'computer'


    else:
        #Computer's turn

        move = getComputerMove(theBoard, computerLetter)
        makeMove(theBoard, computerLetter, move)

        if isWinner(theBoard, computerLetter):
            drawBoard(theBoard)
            print("The computer has beaten you! You lose." )
            gameIsPlaying = False

        else:
             if isBoardFull(theBoard):
                drawBoard(theBoard)
                print("The game is a tie")
                break
             else:
                 turn = 'player'



    print("Do you want to play again?(yes or no)")
    if not input().lower().startswith('y'):
        break