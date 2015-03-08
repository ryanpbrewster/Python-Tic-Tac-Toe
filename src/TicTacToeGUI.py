"""
This class is a GUI for playing Tic Tac Toe

Like the CLI, it uses the TicTacToeBoard and TicTacToeAI modules to handle all
of the logic. This class should only contain logic relating to updating the GUI
- all updates should reflect changes in the TicTacToeBoard class, not changes
made in this class.
"""

from Tkinter import *
import sys
from src.TicTacToeBoard import TicTacToeBoard
from src.TicTacToeAI import TicTacToeAI
import math

class TicTacToeGUI(Frame):
    def __init__(self, master):
        """ This method takes a given Tkinter root and sets up the GUI """
        Frame.__init__(self, master)
        self.width = 600
        self.height = 600
        self.canvasWidth = self.width - 100
        self.canvasHeight = self.height - 100
        self.root = master
        self.root.geometry(str(self.width)+"x"+str(self.height))
        
        self.numPlayers = 1
        self.turn = 0
        self.gameOver = False
        self.TTTAI = TicTacToeAI('O')
        self.gameBoard = TicTacToeBoard()
        
        self.createGame()
        
    def createGame(self):
        """ This method sets or resets the canvas and GUI and is used for creating a new game or for initializing the GUI. """
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
            
    def createRectangles(self):
        """ This method creates the rectangles where tacs are placed. """
        rectangleWidth = (self.canvasHeight / 3)
        rectangleHeight = (self.canvasHeight / 3)
        index = 0
        for p in range(3):
            for i in range(3):
                currentRect = self.gameCanvas.create_rectangle(i * rectangleWidth, p*rectangleHeight, (i * rectangleWidth) + rectangleWidth, (p * rectangleHeight) + rectangleHeight, fill = "black", tag=str(index), outline = 'white')
                self.gameCanvas.tag_bind(currentRect, "<ButtonRelease-1>", self.tacClick)
                index = index + 1
                
    def tacClick(self, event):
        """ Handles placing tacs and swapping the turn when the canvas is clicked. """
        if self.gameOver == False:
            # Determines which rectangle was clicked and gets tac position from that
            rect = self.gameCanvas.find_closest(event.x, event.y)
            tacPosition = int(self.gameCanvas.gettags(rect)[0])
            placed = False
            # Determines where to put tac based on turn, then lets TicTacToe methods handle the rest and calls updateCanvas
            if self.turn == 0:
                placed = self.gameBoard.putTac('X', tacPosition + 1 )
            else:
                placed = self.gameBoard.putTac('O', tacPosition + 1 )
                
            if placed == True:
                self.updateCanvas()
                if not self.gameBoard.checkWin() and not self.gameBoard.checkFull():
                    if self.turn == 1:
                        self.turn = 0
                    else:
                        self.turn = 1
                    if self.numPlayers == 1:
                        self.gameBotMove()
                else:
                    self.gameOver = True
                    self.drawEndGame()
                    
    def gameBotMove(self):
        """ This method wraps the TicTacToeAI botMove method and calls the canvas update method and switches turn. """
        self.TTTAI.botMove(self.gameBoard)
        self.updateCanvas()
        if self.gameBoard.checkWin() or self.gameBoard.checkFull():
            self.gameOver = True
            self.drawEndGame()
        self.turn = 0

        
    def newGame(self):
        """ This method is called by the new game button and clears the canvas and board, resets the turn, and creates the GUI again. """
        self.gameCanvas.delete(ALL)
        self.gameBoard = TicTacToeBoard()
        self.turn = 0
        self.gameOver = False
        self.createGame()
        
    def quit(self):
        """ This is the method called by the quit button to end the game. """
        self.root.quit()
        
    def updateCanvas(self):
        """ Updates the Tkinter canvas based on the TicTacToeBoard object's state"""
        # Checks each board position on TicTacToe board, then sets cooresponding canvas rectangle
        for i in range(9):
            row = math.floor((i ) / 3)
            col = ((i) % 3)
            changeRect = self.gameCanvas.find_withtag(str(i+1))
            if self.gameBoard.TTTBoard[i] == 'X':
                self.gameCanvas.itemconfig(changeRect, fill = "red")
                positionX = (col * 166) + 83
                positionY = (row * 166) + 83
                self.gameCanvas.create_text(positionX, positionY, font=("Arial", 20), text="X", fill="black" )
            elif self.gameBoard.TTTBoard[i] == 'O':
                self.gameCanvas.itemconfig(changeRect, fill = "blue")
                positionX = (col * 166) + 83
                positionY = (row * 166) + 83
                self.gameCanvas.create_text(positionX, positionY, font=("Arial", 20), text="O", fill="white"  )
            else:
                self.gameCanvas.itemconfig(changeRect, fill = "black") 

    def drawEndGame(self):
        """ Draws a status to the board depending on how the game ended. """
        if self.gameBoard.checkWin():
            if self.turn == 1:
                self.gameCanvas.create_text((math.floor(self.canvasWidth/2), math.floor(self.canvasHeight / 2)), font=("Arial", 30), fill = 'green', text="Blue wins!")
            else: 
                self.gameCanvas.create_text((math.floor(self.canvasWidth/2), math.floor(self.canvasHeight / 2)), font=("Arial", 30), fill = 'green', text="Red wins!")
        elif self.gameBoard.checkFull():
            self.gameCanvas.create_text((math.floor(self.canvasWidth/2), math.floor(self.canvasHeight / 2)), font=("Arial", 30), fill = 'green', text="Game Draw!")
            
