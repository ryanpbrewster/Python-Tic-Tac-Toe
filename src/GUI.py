"""
This class is a GUI for playing Tic Tac Toe

Like the CLI, it uses the LargeBoard and AI modules to handle all of the logic.
This class should only contain logic relating to updating the GUI - all updates
should reflect changes in the TicTacToeBoard class, not changes made in this
class.
"""

from tkinter import *
import sys
from src.SmallBoard import SmallBoard
from src.LargeBoard import LargeBoard
from src.AI import AI
import math

class GUI(Frame):
    PLAYER_COLOR_MAP = { 0 : "red", 1 : "blue" }
    def __init__(self, root):
        """
        Sets up the necessary data members, then opens the main menu
        """
        print("Initializing the GUI")
        Frame.__init__(self, root)

        # A large board is a 3x3 array of small boards
        # a small board is a 3x3 array of cells

        self.dims = dict()
        self.dims["cell_width"]  = 60
        self.dims["cell_height"] = 60
        self.dims["cell_hpad"]   = 0 # horizontal padding between cells
        self.dims["cell_vpad"]   = 0 # vertical padding between cells
        self.dims["sb_width"]    = 3*self.dims["cell_width"]  + 2*self.dims["cell_hpad"]
        self.dims["sb_height"]   = 3*self.dims["cell_height"] + 2*self.dims["cell_vpad"]
        self.dims["sb_hpad"]     = 50 # horizontal padding between small boards
        self.dims["sb_vpad"]     = 50 # vertical padding between small boards
        self.dims["lb_width"]    = 3*self.dims["sb_width"]  + 2*self.dims["sb_hpad"]
        self.dims["lb_height"]   = 3*self.dims["sb_height"] + 2*self.dims["sb_vpad"]

        self.window_width = self.dims["lb_width"]
        self.window_height = self.dims["lb_height"] + 50
        self.root = root
        self.root.geometry("%dx%d" % (self.window_width, self.window_height))

        self.frame = None

        print("Calling mainMenu")
        self.mainMenu()

    def mainMenu(self):
        if self.frame != None:
            self.frame.destroy()
        self.frame = MenuFrame(self)
        self.pack()

    def newAIGame(self):
        if self.frame != None:
            self.frame.destroy()
        self.frame = GameFrame(self, self.dims)
        self.pack()

class MenuFrame(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        print("Setting up main menu")
        self.root = root

        self.new_game_button = Button(self, text="Start AI Game", command = self.root.newAIGame)
        self.new_game_button.grid(row = 1)

        self.quit_button = Button(self, text = "Quit", command = self.quit)
        self.quit_button.grid(row=2)

        self.pack()

    def quit(self):
        self.root.quit()

class GameFrame(Frame):
    def __init__(self, root, dims):
        """
        This method sets up a new game board and a new canvas for displaying
        that game board
        """
        Frame.__init__(self, root)
        self.root = root
        self.dims = dims

        self.numPlayers = 1
        self.turn = 0
        self.gameOver = False
        self.ai = AI('O')
        self.game_board = LargeBoard()

        self.game_board = LargeBoard()
        self.turn = 0
        self.gameOver = False

        self.game_canvas = Canvas(self, bg = "black",
                               height = self.dims["lb_height"], width = self.dims["lb_width"])
        self.game_canvas.grid(row = 1)
        self.rects = self.createRectangles()

        self.main_menu_button = Button(self, text="Main Menu", command = self.root.mainMenu)
        self.main_menu_button.grid(row = 2)

        self.pack()

        self.updateCanvas()

    def cellPosition(self, board_pos, cell_pos):
        (i,j) = board_pos
        (ii,jj) = cell_pos
        x = j * (self.dims["sb_width"]  + self.dims["sb_hpad"]) + jj*self.dims["cell_width"]
        y = i * (self.dims["sb_height"] + self.dims["sb_vpad"]) + ii*self.dims["cell_height"]
        return (x,y)

    def createRectangles(self):
        """
        A bunch of tkinter calls that set up the canvas on which the game boar
        is displayed
        """
        rects = [[[[None for _ in range(3)] for _ in range(3)] for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                for ii in range(3):
                    for jj in range(3):
                        (x0,y0) = self.cellPosition( (i,j), (ii,jj) )
                        (x1,y1) = (x0 + self.dims["cell_width"], y0 + self.dims["cell_height"])
                        cell_tag = str(i) + str(j) + str(ii) + str(jj)
                        rect = self.game_canvas.create_rectangle(x0, y0, x1, y1,
                                          tag = cell_tag, fill = "white", outline = 'black')
                        self.game_canvas.tag_bind(rect, "<ButtonRelease-1>", self.tacClick)
                        rects[i][j][ii][jj] = rect
        return rects

    def tacClick(self, event):
        """ Handles placing tacs and swapping the turn when the canvas is clicked. """
        if self.gameOver == False:
            # Determines which rectangle was clicked and gets tac position from that
            rect = self.game_canvas.find_closest(event.x, event.y)
            cell_tag = self.game_canvas.gettags(rect)[0]

            [i,j,ii,jj] = map(int, cell_tag)

            board_pos = (i, j)
            cell_pos = (ii, jj)

            # Check to see if we've clicked in the active board
            if not self.game_board.isLegalPlay(board_pos, cell_pos):
                return

            if self.turn == 0:
                self.game_board.putTac('X', board_pos, cell_pos)
            else:
                self.game_board.putTac('O', board_pos, cell_pos)

            self.updateCanvas()
            if not self.game_board.hasWinner() and not self.game_board.isFull():
                if self.turn == 1:
                    self.turn = 0
                else:
                    self.turn = 1
                if self.numPlayers == 1:
                    self.gameBotMove()
            else:
                print("The game is over")
                if self.game_board.hasWinner():
                    print("We have a winner")
                else:
                    print("Board is full")
                self.gameOver = True
                self.drawEndGame()

    def gameBotMove(self):
        """ This method wraps the AI botMove method and calls the canvas update method and switches turn. """
        move_board, move_pos = self.ai.chooseMove(self.game_board)
        self.game_board.putTac(self.ai.tac, move_board, move_pos)
        self.updateCanvas()
        if self.game_board.hasWinner() or self.game_board.isFull():
            self.gameOver = True
            self.drawEndGame()
        self.turn = 0


    def quit(self):
        """ This is the method called by the quit button to end the game. """
        self.root.quit()


    def updateCanvas(self):
        """ Updates the Tkinter canvas based on the Board object's state"""
        # Draw each board

        player_color = GUI.PLAYER_COLOR_MAP[self.game_board.active_player]
        for i in range(3):
            for j in range(3):
                if self.game_board.boards[i][j].hasWinner():
                    winner = self.game_board.boards[i][j].winner()
                    color = "red" if winner == "X" else "blue"
                    self.fillBoard((i,j), color)
                else:
                    self.drawCells((i,j))

                if self.game_board.isActive((i,j)):
                    self.outlineBoard((i,j), player_color)
                else:
                    self.dimBoard((i,j))

    def fillBoard(self, board_pos, color):
        i, j = board_pos
        for ii in range(3):
            for jj in range(3):
                rect = self.rects[i][j][ii][jj]
                self.game_canvas.itemconfig(rect, fill = color)

    def drawCells(self, board_pos):
        i, j = board_pos
        for ii in range(3):
            for jj in range(3):
                rect = self.rects[i][j][ii][jj]
                if self.game_board.boards[i][j].board[ii][jj] == 'X':
                    self.game_canvas.itemconfig(rect, fill = "red")
                elif self.game_board.boards[i][j].board[ii][jj] == 'O':
                    self.game_canvas.itemconfig(rect, fill = "blue")

    def outlineBoard(self, board_pos, color):
        i, j = board_pos
        for ii in range(3):
            for jj in range(3):
                rect = self.rects[i][j][ii][jj]
                self.game_canvas.itemconfig(rect, outline = color)

    def dimBoard(self, board_pos):
        self.outlineBoard(board_pos, "white")


    def drawEndGame(self):
        """ Draws a status to the board depending on how the game ended. """
        if self.game_board.hasWinner():
            if self.turn == 1:
                self.game_canvas.create_text((math.floor(self.canvasWidth/2), math.floor(self.canvasHeight / 2)), font=("Arial", 30), fill = 'green', text="Blue wins!")
            else: 
                self.game_canvas.create_text((math.floor(self.canvasWidth/2), math.floor(self.canvasHeight / 2)), font=("Arial", 30), fill = 'green', text="Red wins!")
        elif self.game_board.isFull():
            self.game_canvas.create_text((math.floor(self.canvasWidth/2), math.floor(self.canvasHeight / 2)), font=("Arial", 30), fill = 'green', text="Game Draw!")
