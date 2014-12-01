import random


def printBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')


def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

        return ['X', 'O']
    else:
        return ['O', 'X']


def whoGoesFirst():

    return 'player'
    #Let's hardcode it!


def wannaPlayAgain():

    print('Do you want to play one more game, dude? (type yes or no)')
    if input().lower().startswith('y'):
        return True


def makeMove(board, letter, move):
    board[move] = letter

def isWinner(board, letter):

    return ((board[7] == letter and board[8] == letter and board[9] == letter) or
    (board[4] == letter and board[5] == letter and board[6] == letter) or
    (board[1] == letter and board[2] == letter and board[3] == letter) or
    (board[7] == letter and board[4] == letter and board[1] == letter) or
    (board[8] == letter and board[5] == letter and board[2] == letter) or
    (board[9] == letter and board[6] == letter and board[3] == letter) or
    (board[7] == letter and board[5] == letter and board[3] == letter) or
    (board[9] == letter and board[5] == letter and board[1] == letter))


def copyPlayingBoard(board):

    duplicateBoard = []

    for element in board:
        duplicateBoard.append(element)

    return duplicateBoard


def freeSpaceCheck(board, move):

    return board[move] == ' '


def getPlayerMove(board):

    playerMove = ' '
    while playerMove not in '1 2 3 4 5 6 7 8 9'.split() or not freeSpaceCheck(board, int(playerMove)):
        print('What is your next move? (1-9)')
        playerMove = input()
    return int(playerMove)


def chooseRandomMoveFromList(board, possibleMovesList):

    possibleMoves = []
    for move in possibleMovesList:
        if freeSpaceCheck(board, move):
            possibleMoves.append(move)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None


def getComputerMove(board, computerLetter):

    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    #AI, MUAHAHAHHAAH
    for i in range(1, 10):
        playingBoardCopy = copyPlayingBoard(board)
        if freeSpaceCheck(playingBoardCopy, i):
            makeMove(playingBoardCopy, computerLetter, i)
            if isWinner(playingBoardCopy, computerLetter):
                return i

    # Check if the player could win on his next move, and block them.
    for i in range(1, 10):
        playingBoardCopy = copyPlayingBoard(board)
        if freeSpaceCheck(playingBoardCopy, i):
            makeMove(playingBoardCopy, playerLetter, i)
            if isWinner(playingBoardCopy, playerLetter):
                return i

    # Try to take one of the corners, if they are free.
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    # Try to take the center, if it is free.
    if freeSpaceCheck(board, 5):
        return 5

    # Move on one of the sides.
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])


def isBoardFull(board):
    for block in range(1, 10):
        if freeSpaceCheck(board, block):
            return False
    return True


def printRules():
    print("Here are the rules: ")
    print("--------------------------------------")
    print("The board's blocks are in the rnge from 1-9. ")
    print("Write the number of the block you want to put your letter")
    print("Wait for computer's move and then if you're still in the game")
    print("enter your next turn.")
    print("Enter correct numbers, homo! I will check anyway...")
    print("ENJOY THE GAME! IF YOU LOOSE, DON'T DESTROY YOUR PC!")
    print("--------------------------------------")


print('Tic-Tac-Toe Hack Edition!')
printRules()

while True:#  Fire-up the infinite loop, baby!
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print("Okay, HackerBoy, you're first!")
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            # Player's turn.
            printBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                printBoard(theBoard)
                print("Shiet son, you're good! YOU WIN! ")
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    printBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'

        else:
            # Computer's turn.
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                printBoard(theBoard)
                print('Hahahaha, sucker! The computer has beaten you! You LOSE.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    printBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'

    if not wannaPlayAgain():
        print("Get the hell out of here!")
        break
