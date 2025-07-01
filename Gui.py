import os
import sys
import stddraw
import stdarray
import copy
from color import Color
from picture import Picture

class Gui():

    def __init__(self ):
        self.CANVAS_HEIGHT = 1000
        self.CANVAS_WIDTH = 1200
        self.size = 3
        self.read_pics()
        stddraw.setCanvasSize(self.CANVAS_WIDTH, self.CANVAS_HEIGHT)

    def create_board(self, board, winner):
        stddraw.setPenColor(stddraw.WHITE)
        stddraw.setXscale(0, self.CANVAS_WIDTH)
        stddraw.setYscale(0, self.CANVAS_HEIGHT)
        stddraw.filledRectangle(0, 0, self.CANVAS_HEIGHT, self.CANVAS_WIDTH)
        stddraw.setPenColor(stddraw.BLACK)
        stddraw.setPenRadius(3)

        #draw box
        stddraw.line(50, 50, 50, self.CANVAS_HEIGHT - 50)
        #stddraw.line(self.CANVAS_WIDTH - 400, self.CANVAS_HEIGHT - 50, self.CANVAS_WIDTH - 400, 50)
        stddraw.line(50, self.CANVAS_HEIGHT - 50, self.CANVAS_WIDTH - 350, self.CANVAS_HEIGHT - 50)
        stddraw.line(50, 50, self.CANVAS_WIDTH - 350, 50)

        # draw vertical lines
        partition = (self.CANVAS_WIDTH - 500) / self.size
        for i in range(1, 4):
            stddraw.line(50 + ((self.CANVAS_WIDTH - 400)/3) * i, 50, 50 + ((self.CANVAS_WIDTH - 400)/3) * i, self.CANVAS_HEIGHT - 50) 

        # draw horizontal lines
        for i in range(1, 4):
            stddraw.line(50, 50 + ((self.CANVAS_HEIGHT - 100)/3) * i, self.CANVAS_WIDTH - 350,  50 + ((self.CANVAS_HEIGHT - 100)/3) * i)

        self.place_icons(board, winner)

    def place_icons(self, board, winner):
        duration = 100
        for i in range(self.size):
            for j in range(self.size):
                if board[i][j] == "O":
                     stddraw.picture(self.O, 175 + ((self.CANVAS_WIDTH - 400)/3) * j, 200 + ((self.CANVAS_HEIGHT - 100)/3) * i)
                elif board[i][j] == "X":
                    stddraw.picture(self.X, 175 + ((self.CANVAS_WIDTH - 400)/3) * j, 200 + ((self.CANVAS_HEIGHT - 100)/3) * i)
                else:
                    continue
        if winner:
            duration = 10000
            stddraw.picture(self.winner, self.CANVAS_WIDTH/ 2, self.CANVAS_HEIGHT/2)
        stddraw.show(duration)

    def read_pics(self):
        self.X = Picture(os.path.join("./assets_gui/", "X.png"))
        self.O = Picture(os.path.join("./assets_gui/", "O.png"))
        self.winner = Picture(os.path.join("./assets_gui/", "Winner.png"))
