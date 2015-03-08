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
    def __init__(self, master):
        """ This method takes a given Tkinter root and sets up the GUI """
        Frame.__init__(self, master)

        self.cell_width   = 60
        self.cell_height  = 60
        self.board_width  = 3*self.cell_width
        self.board_height = 3*self.cell_width

        self.horizontal_pad = 50
        self.vertical_pad  = 50

        self.width = 3*self.board_width + 2*self.horizontal_pad
        self.height = 3*self.board_height + 2*self.vertical_pad

        self.canvasWidth = self.width
        self.canvasHeight = self.height
        self.root = master
        self.root.geometry(str(self.width)+"x"+str(self.height))

        self.numPlayers = 1
        self.turn = 0
        self.gameOver = False
        self.ai = AI('O')
        self.game_board = LargeBoard()

        self.createGame()

    def createGame(self):
        """
        This method sets or resets the canvas and GUI and is used for creating
        a new game or for initializing the GUI.
        """
        self.columnconfigure(0, pad = 5)
        self.columnconfigure(1, pad = 5)
        self.rowconfigure(0, pad = 10)
        self.rowconfigure(1, pad = 10)
        self.numPlayersField = Entry(self)
        self.numPlayersField.insert(0,"1")
        self.setPlayersButton = Button(self, text = "Set number of players", command = self.setPlayers)
        self.numPlayersField.grid(row=0, column = 0)
        self.setPlayersButton.grid(row=0, column = 1)
        self.gameCanvas = Canvas(self, bg = "black", height = self.canvasHeight, width = self.canvasWidth)
        self.gameCanvas.grid(row = 1, column = 0, columnspan = 2)
        self.newGameButton = Button(self, text="New game", command = self.newGame)
        self.quitGameButton = Button(self, text="Quit", command = self.quit)
        self.newGameButton.grid(row = 2, column = 0)
        self.quitGameButton.grid(row = 2, column = 1)
        self.pack()
        self.createRectangles()
    
    def setPlayers(self):
        """ This method is called by the set players button to set the number of players. """
        tempNum = int(self.numPlayersField.get())
        if tempNum == 1 or tempNum == 2:
            self.numPlayers = int(self.numPlayersField.get())

    def cellPosition(self, board_pos, cell_pos):
        (i,j) = board_pos
        (ii,jj) = cell_pos
        x = j * (self.board_width + self.horizontal_pad) + jj*self.cell_width
        y = i * (self.board_height + self.vertical_pad) + ii*self.cell_height
        return (x,y)

    def createRectangles(self):
        """
        A bunch of tkinter calls that set up the canvas on which the game boar
        is displayed
        """
        for i in range(3):
            for j in range(3):
                for ii in range(3):
                    for jj in range(3):
                        cell_tag = str(i) + str(j) + str(ii) + str(jj)
                        (x,y) = self.cellPosition( (i,j), (ii,jj) )
                        currentRect = self.gameCanvas.create_rectangle(x, y, x+self.cell_width, y+self.cell_height,
                                          fill = "white", tag=cell_tag, outline = 'black')
                        print("Made (%d,%d) (%d,%d) with tag %s"%(i,j,ii,jj,cell_tag))
                        self.gameCanvas.tag_bind(currentRect, "<ButtonRelease-1>", self.tacClick)

    def tacClick(self, event):
        """ Handles placing tacs and swapping the turn when the canvas is clicked. """
        if self.gameOver == False:
            # Determines which rectangle was clicked and gets tac position from that
            rect = self.gameCanvas.find_closest(event.x, event.y)
            cell_tag = self.gameCanvas.gettags(rect)[0]
            print("CLICKING! TAG =", cell_tag)

            [i,j,ii,jj] = map(int, cell_tag)

            board_pos = (i, j)
            cell_pos = (ii, jj)

            print("Board pos = ", board_pos)
            print("Cell pos = ", cell_pos)

            # Check to see if we've clicked in the active board
            if not self.game_board.isLegalPlay(board_pos, cell_pos):
                print("That move is illegal, setting it to black")
                self.gameCanvas.itemconfig(rect, fill="black")
                return

            if self.turn == 0:
                print("GUI decided on X")
                self.game_board.putTac('X', board_pos, cell_pos)
            else:
                print("GUI decided on O")
                self.game_board.putTac('O', board_pos, cell_pos)

            self.updateCanvas()
            print("Done updating canvas")
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
        print("The AI put down a %s"%self.ai.tac)
        self.updateCanvas()
        if self.game_board.hasWinner() or self.game_board.isFull():
            self.gameOver = True
            self.drawEndGame()
        self.turn = 0


    def newGame(self):
        """ This method is called by the new game button and clears the canvas and board, resets the turn, and creates the GUI again. """
        self.gameCanvas.delete(ALL)
        self.game_board = LargeBoard()
        self.turn = 0
        self.gameOver = False
        self.createGame()
        
    def quit(self):
        """ This is the method called by the quit button to end the game. """
        self.root.quit()
        
    def updateCanvas(self):
        """ Updates the Tkinter canvas based on the Board object's state"""
        # Checks each board position on TicTacToe board, then sets cooresponding canvas rectangle
        for i in range(3):
            for j in range(3):
                for ii in range(3):
                    for jj in range(3):
                        cell_tag = str(i) + str(j) + str(ii) + str(jj)
                        rect = self.gameCanvas.find_withtag(cell_tag)
                        if self.game_board.boards[i][j].board[ii][jj] == 'X':
                            print("Found X at (%d,%d), (%d,%d), setting to red" % (i,j,ii,jj))
                            self.gameCanvas.itemconfig(rect, fill = "red")
                        elif self.game_board.boards[i][j].board[ii][jj] == 'O':
                            self.gameCanvas.itemconfig(rect, fill = "blue")
                            print("Found O at (%d,%d), (%d,%d), setting to blue" % (i,j,ii,jj))
                        else:
                            self.gameCanvas.itemconfig(rect, fill = "white")
        foo = self.gameCanvas.find_withtag("2222")
        self.gameCanvas.itemconfig(foo, fill = "black")

    def drawEndGame(self):
        """ Draws a status to the board depending on how the game ended. """
        if self.game_board.hasWinner():
            if self.turn == 1:
                self.gameCanvas.create_text((math.floor(self.canvasWidth/2), math.floor(self.canvasHeight / 2)), font=("Arial", 30), fill = 'green', text="Blue wins!")
            else: 
                self.gameCanvas.create_text((math.floor(self.canvasWidth/2), math.floor(self.canvasHeight / 2)), font=("Arial", 30), fill = 'green', text="Red wins!")
        elif self.game_board.isFull():
            self.gameCanvas.create_text((math.floor(self.canvasWidth/2), math.floor(self.canvasHeight / 2)), font=("Arial", 30), fill = 'green', text="Game Draw!")
            
