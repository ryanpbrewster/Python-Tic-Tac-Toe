from tkinter import *
from TicTacToeBoard import *
from TicTacToeAI import *
import math

class TTTGame(Frame):
	def __init__(self, master):
		Frame.__init__(self, master)
		self.width = 600
		self.height = 600
		self.canvasWidth = self.width - 100
		self.canvasHeight = self.height - 100
		root.geometry(str(self.width)+"x"+str(self.height))
		
		self.numPlayers = 1
		self.turn = 0
		self.gameOver = False
		self.TTTAI = TicTacToeAI('O')
		self.gameBoard = TicTacToeBoard()
		
		self.createGame()
		
	def createGame(self):
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
		tempNum = int(self.numPlayersField.get())
		if tempNum == 1 or tempNum == 2:
			self.numPlayers = int(self.numPlayersField.get())
	def createRectangles(self):
		rectangleWidth = (self.canvasHeight / 3)
		rectangleHeight = (self.canvasHeight / 3)
		index = 0
		for p in range(3):
			for i in range(3):
				currentRect = self.gameCanvas.create_rectangle(i * rectangleWidth, p*rectangleHeight, (i * rectangleWidth) + rectangleWidth, (p * rectangleHeight) + rectangleHeight, fill = "black", tag=str(index), outline = 'white')
				self.gameCanvas.tag_bind(currentRect, "<ButtonRelease-1>", self.tacClick)
				index = index + 1
				
	def tacClick(self, event):
		# Only works if game is not over
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
				if self.turn == 1:
					self.turn = 0
				else:
					self.turn = 1
				if self.numPlayers == 1:
					self.gameBotMove()
					
	def gameBotMove(self):
		self.TTTAI.botMove(self.gameBoard)
		self.updateCanvas()
		self.turn = 0
		
	def newGame(self):
		self.gameCanvas.delete(ALL)
		self.gameBoard = TicTacToeBoard()
		self.turn = 0
		self.gameOver = False
		self.createGame()
		
	def quit(self):
		root.quit()
		
	def updateCanvas(self):
		# Checks each board position on TicTacToe board, then sets cooresponding canvas rectangle
		for i in range(9):
			changeRect = self.gameCanvas.find_withtag(str(i+1))
			if self.gameBoard.TTTBoard[i] == 'X':
				self.gameCanvas.itemconfig(changeRect, fill = "red")
			elif self.gameBoard.TTTBoard[i] == 'O':
				self.gameCanvas.itemconfig(changeRect, fill = "blue")
			else:
				self.gameCanvas.itemconfig(changeRect, fill = "black") 

		# Calls checkWin first (because a full board and a win are possible at the same time)
		if self.gameBoard.checkWin():
			if self.turn == 1:
				self.gameCanvas.create_text((math.floor(self.canvasWidth/4), math.floor(self.canvasHeight / 5)), fill = 'white', text="Blue wins!")
			else: 
				self.gameCanvas.create_text((math.floor(self.canvasWidth/4), math.floor(self.canvasHeight / 5)), fill = 'white', text="Red wins!")
			self.gameOver = True
		elif self.gameBoard.checkFull():
			self.gameCanvas.create_text((math.floor(self.canvasWidth/4), math.floor(self.canvasHeight / 5)), fill = 'white', text="Game Draw!")
			self.gameOver = True
		
root = Tk()
root.wm_title("Play TicTacToe!")
TTT = TTTGame(root)
root.mainloop()
