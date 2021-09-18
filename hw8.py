import math, copy, random
from cmu_112_graphics import *


iPiece = [
    [  True,  True,  True,  True ]
]

jPiece = [
    [  True, False, False ],
    [  True,  True,  True ]
]

lPiece = [
    [ False, False,  True ],
    [  True,  True,  True ]
]

oPiece = [
    [  True,  True ],
    [  True,  True ]
]

sPiece = [
    [ False,  True,  True ],
    [  True,  True, False ]
]

tPiece = [
    [ False,  True, False ],
    [  True,  True,  True ]
]

zPiece = [
    [  True,  True, False ],
    [ False,  True,  True ]
]

tetrisPieces = [ iPiece, jPiece, lPiece, oPiece, sPiece, tPiece, zPiece ]
tetrisPieceColors = [ "red", "yellow", "magenta", "pink", "cyan", "green", "orange" ]


def appStarted(app):
    (width, height, rows, cols, cellSize, margin) = gameDimensions()
    app.rows = rows
    app.cols = cols
    app.cellSize = cellSize
    app.margin = margin
    app.board = [["blue" for i in range(cols)] for j in range(rows)]
    app.defaultColor = "blue"
    app.tetrisPieces = tetrisPieces
    app.tetrisPieceColors = tetrisPieceColors

    # for testing remove later
    app.board[0][0] = "red"
    app.board[0][cols-1] = "white"
    app.board[rows-1][0] = "green"
    app.board[rows-1][cols-1] = "gray"
    newFallingPiece(app)

def keyPressed(app, event):
    if event.key == "Left":
        moveFallingPiece(app, 0, -1)
    if event.key ==  "Right":
        moveFallingPiece(app, 0, 1)
    if event.key == "Up":
        moveFallingPiece(app, -1, 0)    
    if event.key == "Down":
        moveFallingPiece(app, 1, 0)    

def isLegal(app):
    for i in range(len(app.fallingPiece)):
        for j in range(len(app.fallingPiece[0])):
            if app.fallingPieceCol + j >= app.cols or app.fallingPieceRow+ i >= app.rows or app.fallingPieceCol + j < 0 or app.fallingPieceRow + i < 0:
                return False
            if app.fallingPiece[i][j] == True:
                if app.board[i + app.fallingPieceRow][j + app.fallingPieceCol] != app.defaultColor:
                    return False
    return True

def moveFallingPiece(app, drow, dcol):
    app.fallingPieceCol += dcol
    app.fallingPieceRow += drow
    if isLegal(app) == False:
        app.fallingPieceCol -= dcol
        app.fallingPieceRow -= drow



def newFallingPiece(app):
    randomIdx = random.randint(0, len(app.tetrisPieces) - 1)
    app.fallingPiece = app.tetrisPieces[randomIdx]
    app.fallingPieceColor = app.tetrisPieceColors[randomIdx]
    app.fallingPieceRow = 0
    app.fallingPieceCol = app.cols // 2 - len(app.fallingPiece[0]) // 2
     

def drawFallingPiece(app, canvas):
    piece = app.fallingPiece
    for i in range(len(piece)):
        for j in range(len(piece[0])):
            if piece[i][j] == True:
                drawCell(app, canvas, i + app.fallingPieceRow, j + app.fallingPieceCol, app.fallingPieceColor)


def drawCell(app, canvas, i, j, color):
    canvas.create_rectangle(app.margin + app.cellSize * j, app.margin + app.cellSize * i, app.margin + app.cellSize * (j + 1), app.margin + app.cellSize * (i + 1), fill = color)


def drawboard(app, canvas):
    for i in range(app.rows):
        for j in range(app.cols):
            drawCell(app, canvas, i, j, app.board[i][j])

def redrawAll(app, canvas):
    drawboard(app, canvas)
    drawFallingPiece(app, canvas)


                       

def playTetris():
    print('Replace this with your Tetris game!')
    (width, height, rows, cols, cellSize, margin) = gameDimensions()
    runApp(width = width, height = height)    


class Tetris(object):
    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.cellSize = 0
        self.margin = 0
#################################################
# main
#################################################

def gameDimensions():
    tetris = Tetris()
    tetris.rows = 15
    tetris.cols = 10
    tetris.cellSize = 20
    tetris.margin = 25
    width = tetris.margin *2 + tetris.cols * tetris.cellSize
    height = tetris.margin *2 + tetris.rows * tetris.cellSize
    return (width, height, tetris.rows, tetris.cols, tetris.cellSize, tetris.margin)
def main():
    playTetris()

if __name__ == '__main__':
    main()
