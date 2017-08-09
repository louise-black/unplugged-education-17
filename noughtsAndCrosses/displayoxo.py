import pygame
import sys
import os


coordinates = coordinates = {
    1:[1,1],
    2:[12,1],
    3:[23,1],
    4:[1,12],
    5:[12,12],
    6:[23,12],
    7:[1,23],
    8:[12,23],
    9:[23,23]
}

def drawBoard():
    with open('screen.dat', 'w') as f:
        f.write('DISPLAY_DL_SEL 1 \n')
        f.write('DISPLAY_REG 10000000000000000000000000000000  00000000000000000000000000000000  00000000000000000000000000000000  00000000000000000000000000000000  00000000000000000000000000000000 00000000000000000000000000000000 00000000000000000000000000000000 00000000000000000000000000000000  00000000000000000000000000000000 00000000000000000000000000000000 00000000000000000000000000000000 00000000000000000000000000000000  00000000000000000000000000000000 00000000000000000000000000000000  00000000000000000000000000000000 00000000000000000000000000000000  00000000000000000000000000000000 00000000000000000000000000000000\n')
        f.write('DISPLAY_DL 1 ')
        f.write('00000000001000000000010000000000 00000000001000000000010000000000 00000000001000000000010000000000 00000000001000000000010000000000 00000000001000000000010000000000 00000000001000000000010000000000 00000000001000000000010000000000 00000000001000000000010000000000 00000000001000000000010000000000 00000000001000000000010000000000 11111111111111111111111111111111 00000000001000000000010000000000 00000000001000000000010000000000 00000000001000000000010000000000 00000000001000000000010000000000 00000000001000000000010000000000 00000000001000000000010000000000 00000000001000000000010000000000 00000000001000000000010000000000 00000000001000000000010000000000 00000000001000000000010000000000 11111111111111111111111111111111 00000000001000000000010000000000 00000000001000000000010000000000 00000000001000000000010000000000 00000000001000000000010000000000 00000000001000000000010000000000 00000000001000000000010000000000 00000000001000000000010000000000')
        f.write('00000000001000000000010000000000 00000000001000000000010000000000 00000000001000000000010000000000\n')

    os.system("python display.py screen.dat")


# drawMarker(player, position) where player is in {O,X} and position is in [1..9]
def drawMarker(player, position):
    theLines = []
    #open the file and get the data and store it
    with open("screen.dat", "r+") as q:
        for line in q.readlines():
            dataPoints = line.split()
            if dataPoints[0] == "DISPLAY_DL":
                theLines += dataPoints[2:]
        #delete the line in the file of the old board
        deleteLine()
        #get the coordinates of the new position to be updated in the board
        square = coordinates.get(position)
        if player == 'X':
            # the coordinate from the dictionary
            xcoord = square[0]
            ycoord = square[1]

            otherBlock = xcoord + 7
            #update some bits - just for viewing purposes at the moment

            for i in range(1, 9):
                theRow = list(str(theLines[ycoord]))
                theRow[xcoord] = '1'
                theRow[otherBlock] = '1'
                xcoord += 1
                otherBlock -= 1
                theLines[ycoord] = "".join(theRow)
                ycoord += 1

            #replace it in the file to make a new board
            replacedLine = "DISPLAY_DL 1 " + ' '.join(theLines)
            with open("screen2.dat", "a") as p:
                p.write(replacedLine)

            #call display

        if player == 'O':
            # the coordinate from the dictionary
            xcoord = square[0]
            ycoord = square[1]

            theFirstRow = list(str(theLines[ycoord]))
            theLastRow = list(str(theLines[ycoord + 7]))

            placeX = xcoord
            for i in range(0, 4):
                theFirstRow[placeX + 2] = '1'
                theLastRow[placeX + 2] = '1'
                placeX += 1

            theLines[ycoord] = ''.join(theFirstRow)
            theLines[ycoord + 7] = ''.join(theLastRow)

            theSecondRow = list(str(theLines[ycoord + 1]))
            the8thRow = list(str(theLines[ycoord + 6]))

            theSecondRow[xcoord + 1] = '1'
            the8thRow[xcoord + 1] = '1'
            theSecondRow[xcoord + 6] = '1'
            the8thRow[xcoord + 6] = '1'

            theLines[ycoord + 1] = ''.join(theSecondRow)
            theLines[ycoord + 6] = ''.join(the8thRow)

            j = xcoord + 7
            for s in range(0, 4):
                theMiddleRow = list(str(theLines[ycoord + 2]))
                theMiddleRow[xcoord] = '1'
                theMiddleRow[j] = '1'
                ycoord += 1
                theLines[ycoord + 1] = ''.join(theMiddleRow)

            #replace it in the file to make a new board
            replacedRow = "DISPLAY_DL 1 " + ' '.join(theLines)
            with open("screen2.dat", "a") as p:
                p.write(replacedRow)

            #call display
            os.system("python display.py screen2.dat")

def deleteLine():
    f_in = 'screen.dat'
    f_out = 'screen2.dat'

    ignored_lines = [3]
    with open(f_in, 'r') as fin, open(f_out, 'w') as fout:
        for lineno, line in enumerate(fin, 1):
            if lineno not in ignored_lines:
                fout.write(line)

#drawBoard()
drawMarker('X', 8)
