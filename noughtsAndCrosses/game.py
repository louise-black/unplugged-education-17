#Initialise the board
#Play the game
#Update each board segment as you go on

#Import necessary items
from __future__ import print_function
import pygame
import sys

#To see what block to be in on the pygame block
coordinates = {
    1:[2,2],
    2:[13,2],
    3:[24,2],
    4:[2,13],
    5:[13,13],
    6:[24,13],
    7:[2,24],
    8:[13,24],
    9:[24,24]
}

# Constants for the board
WINDOW_WIDTH  = 1024
WINDOW_HEIGHT = 600

CRT_WIDTH  =  400
CRT_HEIGHT =  400

BIT_WIDTH    = 5
BIT_HEIGHT   = 5
BIT_SPACING  = 10
LINE_SPACING = 8
DISPLAY_REG_LINE_SPACING = 15

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
DIM_GREEN = (0, 50, 0)

FULL_BOARD = 511

def drawX(coord):
    #coordinate is the square in which the x will go in
    x = coord[0]
    y = coord[1]
    print ('XXXXX')


def drawO(coord):
    x = 0
    print ('OOOOOO')

def drawDelayLine(canvas, delayLineData):
    y = 5 # Start in from the edge
    for data in delayLineData:
        x = 5 # Start in from the edge
        drawBoard(canvas, data, x, y)
        y += LINE_SPACING

#Draws an empty board
def drawBoard(canvas, word, x, y):
    data = word
    for n in range(0,32):
        for i in data:
            if i == '1':
                pygame.draw.line(canvas, GREEN, (x, y), (x + BIT_WIDTH, y), BIT_HEIGHT)
            else:
                pygame.draw.line(canvas, DIM_GREEN, (x, y), (x + BIT_WIDTH, y), BIT_HEIGHT)
            x += BIT_SPACING



def gameOver(boards):
    if boards[0] | boards[1] == FULL_BOARD:
        return True
    else:
        return checkWinner(boards[0]) and checkWinner(boards[1])

def score(boards, player):
    if checkWinner(boards[player]):
        # we win
        return 10
    elif checkWinner(boards[1-player]):
        # other player wins
        return -10
    else:
        return 0

def possibleMoves(boards):
    # return list of possible moves, indexes 0 to 8
    moves = []
    emptySquares = (boards[0] | boards[1]) ^ FULL_BOARD
    for i in range(0,9):
        if (emptySquares>>i)&1 == 1:
            moves.append(i)
    return moves

def minimax(boards, depth, player):
    print ("running minimax depth %d for player %s" % (depth, players[player]))
    printBoard(boards,players)
    bestMove = -1;
    bestScore = (-sys.maxint-1) if (player == 1) else sys.maxint # ternary operator
    scores = []  # these two arrays have same indexing -
    moves = []  # i.e. moves[i] results in scores[i]
    if gameOver(boards) or depth==0:
        bestScore = score(boards, player)
        print ("at depth 0, returning [ %d , %d ] "%( bestScore, bestMove))
        return ([bestScore, bestMove])

    # populate the scores array, over all possible moves
    # recurse as necessary
    for move in possibleMoves(boards):
        boards[player] += (2**move)
        scores.append(minimax(boards, depth-1, 1-player))
        moves.append(move)
        # then remove this move from board?
        boards[player] -= (2**move)

    # now the min/max calculation
    ## player 0 is 'X' - maximise for X
    ## player 1 is 'O' - minimise for O
    assert len(scores) > 0
    assert len(moves) == len(scores)
    bestIndex = 0
    if player == 0:
        # This is the max calculation
        for i in range(0,len(scores)):
            if scores[i] == max(scores):
                bestIndex = i
                break
    else:
        # This is the min calculation
        assert player==1
        for i in range(0,len(scores)):
            if scores[i] == min(scores):
                bestIndex = i
                break
    return ([scores[bestIndex], moves[bestIndex]])


def checkWinner(bitboard):
    # check horizontal winners
    horizontal_row = 1+2+4
    for i in range(0,3):
        if bitboard & horizontal_row == horizontal_row:
            return True
        else:
            horizontal_row *= 8
    vertical_row = 1+8+64
    for i in range(0,3):
        if bitboard & vertical_row == vertical_row:
            return True
        else:
            vertical_row *= 2
    diagonal_row = 1+16+256
    if bitboard & diagonal_row == diagonal_row:
        return True
    diagonal_row = 4+16+64
    if bitboard & diagonal_row == diagonal_row:
        return True

    return False

def printBoard(boards, players):
    for i in range(0,9):
        # iterate over squares
        if (boards[0] & 2**i):
            print (players[0], end='')
        elif (boards[1] & 2**i):
            print (players[1], end='')
        else:
            print (" ", end='')
        if (i+1)%3 == 0:
            print ("\n", end='')


# X goes on even turns (and therefore starts at turn==0)
# O goes on odd turns


#Set up the pygame
def initiliasePyGame():
    boards = [0,0]  # xBoard is boards[0], oBoard is boards[1]
    players = ['X', 'O']
    turn = 0
    pygame.init()
    canvas = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)

    boardData = '00000000001000000000010000000000 00000000001000000000010000000000 00000000001000000000010000000000 00000000001000000000010000000000 00000000001000000000010000000000 00000000001000000000010000000000 00000000001000000000010000000000 00000000001000000000010000000000 00000000001000000000010000000000 00000000001000000000010000000000 11111111111111111111111111111111 00000000001000000000010000000000 00000000001000000000010000000000 00000000001000000000010000000000 00000000001000000000010000000000 00000000001000000000010000000000 00000000001000000000010000000000 00000000001000000000010000000000 00000000001000000000010000000000 00000000001000000000010000000000 00000000001000000000010000000000 11111111111111111111111111111111 00000000001000000000010000000000 00000000001000000000010000000000 00000000001000000000010000000000 00000000001000000000010000000000 00000000001000000000010000000000 00000000001000000000010000000000 00000000001000000000010000000000 \
    00000000001000000000010000000000 00000000001000000000010000000000 00000000001000000000010000000000'

    displayRegSurface  = pygame.Surface((CRT_WIDTH, CRT_HEIGHT))
    displayLineSurface = pygame.Surface((CRT_WIDTH, CRT_HEIGHT))

    while True:
        dataPoints = boardData.split()
        if len(dataPoints) > 0:
            delayLineData = dataPoints

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(-1)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit(-1)

        canvas.fill(BLACK)
        drawDelayLine(displayLineSurface, delayLineData)
        canvas.blit(displayLineSurface, (20, 20, 500, 500))
        pygame.display.flip()

        # check whether board is full - if so it's a draw
        if boards[0] & boards[1] == FULL_BOARD:
            print ("drawn game")
            break

        # ask player to make move (and check it is valid)
        print ("Player %s to make a move: " % (players[turn%2]))

        #### NOT WORKING ##### print ("recommended move is %d, for score --" %(((minimax(boards, 1, turn%2))[0])))

        while True:
            move = raw_input()  ## check its an int in range 1..9 inclusive,
            try:
                # check input is int
                move = int(move)
                # check it's in range
                assert (move>0 and move<10)
                # check this square is empty
                square = 2** (move-1)
                for p in range(0,len(boards)):
                    assert boards[p] & square == 0
                break
            except (ValueError, AssertionError):
                print ("invalid move, enter a number between 1 and 9")
                continue
        ## for squares 1..9 (which we map onto 0..8 in the bitboards)
        square = 2** (move-1)
        # put move on board
        boards[turn%2] += square
        pygameMove = coordinates.get(move)

        # print board
        printBoard(boards,players)

        if players[turn%2] == 'X':
            drawX(pygameMove)
        else:
            drawO(pygameMove)

        # then check whether that player has won
        if checkWinner(boards[turn%2]):
            print ("Player %s has won the game" % (players[turn%2]))
            break

        # then loop back to start
        turn += 1
        continue



initiliasePyGame()
