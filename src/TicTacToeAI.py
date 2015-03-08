"""
A class containing all of the logic for an AI that plays TicTacToe

A note on the way the static and non-static methods work in this class:
* Static methods take a board, a tac to check, and a position, and return an evaluation (true or false). 
* Non-static methods, however, are called by an instance of the TicTacToeAI class. These methods are specifically used for making moves
on a board which has been supplied. They're role is more than returning an evaluation: they change the state of the board which they
are supplied with. 
* Basically, methods that are called by an instance of the class are proactive - they change the state of something. Class methods merely
supply information.

"""
import math
from src.TicTacToeBoard import TicTacToeBoard

class TicTacToeAI:
	def __init__(self,tac):
		"""Initializes an AI instance with appropriate tacs. Should only be used if AI is going to play, not for making detections."""
		self.tac = tac
		self.enemyTac = 'X'
		if tac == 'X':
			self.enemyTac = 'O'
	
	
	def makesFork(board, tacToCheck, position):
		"""A function that detects whether or not a given position and given tac makes a fork on a given board."""
		numOfWinningMoves = 0
		testBoard = TicTacToeBoard()
		testBoard.TTTBoard = board.TTTBoard[:]
		if testBoard.putTac(tacToCheck, position):
			# Looks for two or more possible winning moves created by placing a tac at position in question
			for i in range(1, 10):
				if TicTacToeAI.isWinningMove(tacToCheck, testBoard, i):
					numOfWinningMoves = numOfWinningMoves + 1
			if numOfWinningMoves > 1:
				return True
			else:
				return False
		else:
			return False
	
	def isWinningMove(tacToCheck, board, position):
		"""A function that detects whether or not a given position with a given tac makes a win on a given board."""
		testBoard = TicTacToeBoard()
		testBoard.TTTBoard = board.TTTBoard[:]
		if testBoard.putTac(tacToCheck, position):
			if testBoard.checkWin():
				return True
			else:
				return False
		else:
			return False
	
	"""A function that detects whether or not a position makes two in a row. 
	
	This function is primarily used in constructing other functions, such as fork detection and botMove, but can be used for detection.
	
	"""
	
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
		for i in range(row*3, row+3):
			if testBoard.TTTBoard[i] == enemyTac:
				enemyCount = enemyCount + 1
			elif testBoard.TTTBoard[i] == tacToCheck:
				friendlyCount = friendlyCount + 1

		if enemyCount == 0 and friendlyCount == 1:
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
			return True
		else:
			return False	
		
	"""A function that uses an instance of TicTacToeAI to make an appropriate move on the given board
	
	This function utilizes all of the other instance methods available to TicTacToeAI's in order to make a
	move which, if the AI were to continue playing, would prevent a loss. (This is to the best of the AI's 
	ability - if a fork has already been created and there are no two in a row positions, there's nothing the
	AI can do to prevent a loss.)
	
	Order of steps: place at win, prevent enemy win, place at fork, prevent enemy fork by either placing two
	in a row or blocking, place at center, place at opposite corner to an enemy piece, or place at next 
	available position.
	
	"""		
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
		""" Instance method using isWinningMove to have the AI place a tac appropriately. Can be used for blocking enemy wins or making a winning move. """
		for i in range (1, 10):
			if TicTacToeAI.isWinningMove(tacToCheck, board, i):
				board.putTac(self.tac, i)
				return True
		return False
				
	def placeAtFork(self, board, tacToCheck):
		""" Instance method using makesFork to place a tac at a fork according to the given tac. """
		for i in range(1, 10):
			if TicTacToeAI.makesFork(board,self.tac,i):
				board.putTac(self.tac)
				return True
		return False
		
	def placeAtTwoInARow(self, board):
		""" Instance method using makesTwoInARow to place a tac at a spot with two in a row. """
		for i in range(1, 10):
			if TicTacToeAI.makesTwoInARow(self.tac, board, i):
				if board.putTac(self.tac, i):
					return True
		return False
		
	def placeAtOppositeCorner(self, board, position):
		""" Instance method that takes a position and places a tac at the opposite corner. """
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
		""" Instance method that places a tac at the next available spot. """
		for i in range(1, 10):
			if board.putTac(self.tac, i):
				return True
		return False

	
