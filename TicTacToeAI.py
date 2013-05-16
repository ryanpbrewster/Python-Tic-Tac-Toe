''' A note on the way static and non-static methods work in this class:
* Static methods take a board, a tac to check, and a position, and return an evaluation (true or false). 
* Non-static methods, however, are called by an instance of the TicTacToeAI class. These methods are specifically used for making moves
on a board which has been supplied. They're role is more than returning an evaluation: they change the state of the board which they
are supplied with. 
* Basically, methods that are called by an instance of the class are proactive - they change the state of something. Class methods merely
supply information.
'''
import math
from TicTacToeBoard import *

class TicTacToeAI:
	def __init__(self,tac):
		self.tac = tac
		self.enemyTac = 'X'
		if tac == 'X':
			self.enemyTac = 'O'
		
	### Gotta fix this and others. Make it so they DON'T USE SELF FOR TAC, get passed a tac ###
	def makesFork(board, tacToCheck, position):
		numOfWinningMoves = 0
		testBoard = TicTacToeBoard()
		testBoard.TTTBoard = board.TTTBoard[:]
		if testBoard.putTac(tacToCheck, position):
			# Looks for two or more possible winning moves created by placing a tac at position in question
			for i in range(1, 10):
				if TicTacToeAI.isWinningMove(tacToCheck, testBoard, i):
					numOfWinningMoves = numOfWinningMoves + 1
			if numOfWinningMoves > 1:
				print("wut")
				return True
			else:
				return False
		else:
			return False
	
	def isWinningMove(tacToCheck, board, position):
		testBoard = TicTacToeBoard()
		testBoard.TTTBoard = board.TTTBoard[:]
		if testBoard.putTac(tacToCheck, position):
			if testBoard.checkWin():
				return True
			else:
				return False
		else:
			return False
	
	def makesTwoInARow(tacToCheck, board, position):
		enemyTac = 'X'
		if tacToCheck == 'X':
			enemyTac = 'O'
		testBoard = TicTacToeBoard()
		testBoard.TTTBoard = board.TTTBoard[:]
		row = math.floor((position - 1 ) / 3)
		col = ((position-1) % 3)
		friendlyCount = 0
		enemyCount = 0

		# Checks if the row has any enemy tacs or friendly tacs
		for i in range(row, row+2):
			if testBoard.TTTBoard[i] == enemyTac:
				enemyCount = enemyCount + 1
			elif testBoard.TTTBoard[i] == tacToCheck:
				friendlyCount = friendlyCount + 1

		if enemyCount == 0 and friendlyCount == 1:
			print("row")
			return True
			
		enemyCount = 0
		friendlyCount = 0
		
		# Checks if the column has any enemy tacs or friendly tacs
		for i in range(col, col + 7, 3):
			if testBoard.TTTBoard[i] == enemyTac:
				enemyCount = enemyCount + 1
			elif testBoard.TTTBoard[i] == tacToCheck:
				friendlyCount = friendlyCount + 1

		if enemyCount == 0 and friendlyCount == 1:
			print("Col" + str(position) + "_" + str(enemyCount))
			return True
		else:
			return False	
		
	### End of fix region
			
	def botMove(self, board):
		if self.tac == 'X':
			enemyTac = 'O'
		else:
			enemyTac = 'X'
			
		if self.placeAtWinningMove(board, self.tac):
			return True
		elif self.placeAtWinningMove(board, enemyTac):
			return True
		elif self.placeAtFork(board, self.tac):
			return True
		for i in range(1, 10):
			if TicTacToeAI.makesFork(board, enemyTac, i):
				if self.placeAtTwoInARow(board):
					return True
				elif board.putTac(self.tac, i):
					return True
		if board.putTac(self.tac, 5):
			return True
		if self.placeAtOppositeCorner(board, 0): 
			return True
		elif self.placeAtOppositeCorner(board, 2): 
			return True
		elif self.placeAtOppositeCorner(board, 6): 
			return True
		elif self.placeAtOppositeCorner(board, 8): 
			return True
		if self.placeAtNextAvailable(board): 
			return True
			
	# Checks for winning moves for the supplied tac, then places the self tac at a winning move if possible
	def placeAtWinningMove(self, board, tacToCheck):
		for i in range (1, 10):
			if TicTacToeAI.isWinningMove(tacToCheck, board, i):
				board.putTac(self.tac, i)
				return True
		return False
				
	def placeAtFork(self, board, tacToCheck):
		for i in range(1, 10):
			if TicTacToeAI.makesFork(board,self.tac,i):
				board.putTac(self.tac)
				return True
		return False
		
	def placeAtTwoInARow(self, board):
		for i in range(1, 10):
			if TicTacToeAI.makesTwoInARow(self.tac, board, i):
				if board.putTac(self.tac, i):
					return True
		return False
		
	def placeAtOppositeCorner(self, board, position):
		placePosition = 0
		if position == 0:
			placePosition = 9
		elif position == 2:
			placePosition = 7
		elif position == 6:
			placePosition = 3
		elif position == 8:
			placePosition = 0
		if(board.TTTBoard[position]  == self.enemyTac):
			if board.putTac(self.tac, placePosition):
				return True
		return False
			
	def placeAtNextAvailable(self, board):
		for i in range(1, 10):
			if board.putTac(self.tac, i):
				return True
		return False

	