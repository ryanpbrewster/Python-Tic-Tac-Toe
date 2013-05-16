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
		if int(pos) > 0 and int(pos) < 10:
			if(self.TTTBoard[int(pos)-1] == str(pos)):
				self.TTTBoard[int(pos)-1] = tac
				return True
			else:
				return False
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