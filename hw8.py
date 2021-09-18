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
    app.isGameOver = False
    app.score = 0   
    newFallingPiece(app)

def placeFallingPiece(app):
    piece = app.fallingPiece
    for i in range(len(piece)):
        for j in range(len(piece[0])):
            if piece[i][j] == True:
                app.board[i + app.fallingPieceRow][j + app.fallingPieceCol] = app.fallingPieceColor
    removeFullRows(app)

def timerFired(app):
    if not app.isGameOver:
        hasMoved = moveFallingPiece(app, 1, 0)    
        if not hasMoved:
            placeFallingPiece(app)
            newFallingPiece(app) 
            if not isLegal(app):
                app.isGameOver = True    


def keyPressed(app, event):
    if event.key == "Left":
        moveFallingPiece(app, 0, -1)
    if event.key ==  "Right":
        moveFallingPiece(app, 0, 1)
    if event.key == "Up":
        rotateFallingPiece(app)    
    if event.key == "Down":
        moveFallingPiece(app, 1, 0) 
    if app.isGameOver and event.key == "r":
        app.board = [["blue" for i in range(app.cols)] for j in range(app.rows)]
        app.isGameOver = False
    if event.key == "Space":
        for i in range(app.rows):
            moveFallingPiece(app, 1, 0)
            if not isLegal(app):
                break


def rotateFallingPiece(app):
    original = app.fallingPiece
    originalRow = len(app.fallingPiece)
    originalCol = len(app.fallingPiece[0])
    originalFallingPieceRow = app.fallingPieceRow
    originalFallingPieceCol = app.fallingPieceCol

    rotatedPiece = []
    for i in range(originalCol):
        row = []
        for j in range(originalRow):
            row.append(None)            
        rotatedPiece.append(row)
    for i in range(originalRow):
        for j in range(originalCol):
            val = original[i][j]
            rotatedPiece[originalCol - j - 1][i] = val
    app.fallingPiece = rotatedPiece
    app.fallingPieceRow = app.fallingPieceRow + originalRow // 2 - originalCol // 2
    app.fallingPieceCol = app.fallingPieceCol + originalCol // 2 - originalRow // 2
    if not isLegal(app):
        app.fallingPiece = original
        app.fallingPieceRow = originalFallingPieceRow
        app.fallingPieceCol = originalFallingPieceCol

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
        return False
    return True        

def removeFullRows(app):
    fullRows = 0
    newBoard = []
    for row in app.board:
        if app.defaultColor in row:
           newBoard.append(copy.copy(row))
        else:
            fullRows += 1
    for i in range(fullRows):
        newRow = [app.defaultColor for i in range(app.cols)]
        newBoard = [newRow] + newBoard
    app.board = newBoard
    app.score += fullRows ** 2



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
    
    if app.isGameOver:
        canvas.create_text(app.width/2, 20, text = "GAME OVER!" )
    else:
        drawFallingPiece(app, canvas)

    canvas.create_text(app.width/2, 10, text = "SCORE: "+ str(app.score))

                       

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
