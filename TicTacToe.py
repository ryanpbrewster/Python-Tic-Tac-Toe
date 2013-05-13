import math

class TicTacToeBoard:
	def __init__(self):
		self.TTTBoard = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
	# Testing purposes only - game should be run with Tkinter GUI
	def printBoard(self):
		for i in range(0,4,3):
			print(self.TTTBoard[i] + " | " + self.TTTBoard[i+1] + " | " + self.TTTBoard[i+2])
			print("--+---+--")
		print(self.TTTBoard[6] + " | " + self.TTTBoard[7] + " | " + self.TTTBoard[8] + "\n")
	
	def putTac(self, tac, pos):
		# Checks if the board at that position is still set to its default value before placing a tac
		if(self.TTTBoard[int(pos)-1] == str(pos)):
			self.TTTBoard[int(pos)-1] = tac
			return True
		else:
			return False
			
	def checkWin(self):
		# Checks if any column has three in a row
		for i in range(0,3):
			if(self.TTTBoard[i] == self.TTTBoard[i+3] and self.TTTBoard[i] == self.TTTBoard[i + 6]):
				return True
		# Checks if any row has three in a row
		for i in range(0, 7, 3):
			if(self.TTTBoard[i] == self.TTTBoard[i+1] and self.TTTBoard[i] == self.TTTBoard[i+2]):
				return True
		# Checks the diagonals
		for i in range(0,3,2):
			if(self.TTTBoard[i] == self.TTTBoard[i + (4 - i)] and self.TTTBoard[i] == self.TTTBoard[i + (2 * (4 - i))]):
				return True
		return False
		
	def checkFull(self):
		for i in self.TTTBoard:
			if i != 'X' and i != 'O':
				return False
		return True
		
	def makeMovePrompt(self, tac):
		print(tac + ", please select a position to place your tac.")
		position = input()
		while(not self.putTac(tac, position)):
			position = input("That move is entirely invalid. Please, try again: ")
			
	def botMove(self, tac):
		if tac == 'X':
			enemyTac = 'O'
		else:
			enemyTac = 'X'
		# Check self winning moves, then place tac at winning move
		for i in range(1, 10):
			if self.isWinningMove(tac, i):
				self.putTac(tac, i)
				return True
		# Check enemy winning moves, then place tac at enemy winning moves
		for i in range(1, 10):
			if self.isWinningMove(enemyTac, i):
				self.putTac(tac, i)
				return True
		# Check possible fork moves, then place tac to create fork
		for i in range(1, 10):
			if self.makesFork(tac, i):
				self.putTac(tac, i)
				return True
		# Check for possible enemy forks, then block them
		for i in range(1, 10):
			if self.makesFork(enemyTac, i):
				# First, look for a place to put two in a row:
				for p in range(1, 10):
					if self.makesTwoInARow(tac, p):
						if self.putTac(tac, p):
							return True
				# If none, prevent enemy fork
				if self.putTac(tac, i):
					return True
		# Try the center
		if self.putTac(tac,5):
			return True
		#Play opposite corner from opponent
		if self.TTTBoard[0] == enemyTac:
			if self.putTac(tac, 9):
				return True
		elif self.TTTBoard[2] == enemyTac:
			if self.putTac(tac, 7):
				return True
		elif self.TTTBoard[6] == enemyTac:
			if self.putTac(tac, 3):
				return True
		elif self.TTTBoard[8] == enemyTac:
			if self.putTac(tac, 0):
				return True
		# Or just place a tac at the next available spot
		for i in range(1, 10):
			if self.putTac(tac, i):
				return True
		
	# Checks if a position creates a win by creating a duplicate board, placing a tac at the position, and calling checkWin()	
	def isWinningMove(self, tac, position):
		board = TicTacToeBoard()
		board.TTTBoard = self.TTTBoard[:]
		if board.putTac(tac, position):
			if board.checkWin():
				return True
			else:
				return False
		else:
			return False
	
	# Used for fork prevention exclusively. 
	def makesTwoInARow(self, tac, position):
		if tac == 'X':
			enemyTac = 'O'
		else:
			enemyTac = 'X'
		board = TicTacToeBoard()
		board.TTTBoard = self.TTTBoard[:]
		row = math.floor((position - 1 ) / 3)
		col = ((position-1) % 3)
		friendlyCount = 0
		enemyCount = 0

		# Checks if the row has any enemy tacs or friendly tacs
		for i in range(row, row+2):
			if board.TTTBoard[i] == enemyTac:
				enemyCount = enemyCount + 1
			elif board.TTTBoard[i] == tac:
				friendlyCount = friendlyCount + 1

		if enemyCount == 0 and friendlyCount == 1:
			return True
			
		enemyCount = 0
		
		# Checks if the column has any enemy tacs or friendly tacs
		for i in range(col, col + 6, 3):
			if board.TTTBoard[i] == enemyTac:
				enemyCount = enemyCount + 1
			elif board.TTTBoard[i] == tac:
				friendlyCount = friendlyCount + 1

		if enemyCount == 0 and friendlyCount == 1:
			return True
		else:
			return False


				
	# Checks for forks
	def makesFork(self, tac, position):
		numOfWinningMoves = 0
		board = TicTacToeBoard()
		board.TTTBoard = self.TTTBoard[:]
		if board.putTac(tac, position):
			# Looks for two or more possible winning moves created by placing a tac at position in question
			for i in range(1, 10):
				if board.isWinningMove(tac, i):
					numOfWinningMoves = numOfWinningMoves + 1
			if numOfWinningMoves > 1:
				return True
			else:
				return False
		else:
			return False
		

		