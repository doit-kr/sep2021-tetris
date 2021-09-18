import math, copy, random

from cmu_112_graphics import *

def appStarted(app):
    (width, height, rows, cols, cellSize, margin) = gameDimensions()
    app.rows = rows
    app.cols = cols
    app.cellSize = cellSize
    app.margin = margin
    app.board = [["blue" for i in range(cols)] for j in range(rows)]
    app.defaultColor = "blue"
    
    # for testing remove later
    app.board[0][0] = "red"
    app.board[0][cols-1] = "white"
    app.board[rows-1][0] = "green"
    app.board[rows-1][cols-1] = "gray"

def drawCell(app, canvas, i, j):
    canvas.create_rectangle(app.margin + app.cellSize * j, app.margin + app.cellSize * i, app.margin + app.cellSize * (j + 1), app.margin + app.cellSize * (i + 1), fill = app.board[i][j])


def drawboard(app, canvas):
    for i in range(app.rows):
        for j in range(app.cols):
            drawCell(app, canvas, i, j)

def redrawAll(app, canvas):
    
    drawboard(app, canvas)

                       

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
