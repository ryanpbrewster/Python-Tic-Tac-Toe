from TicTacToeBoard import *
from TicTacToeAI import *

class TicTacToeCLI:
	def __init__(self):
		self.GameBoard = TicTacToeBoard()
	def runGame(self):
		playing = True
		while(playing):
			#Set up game....
			players = self.getNumPlayers()
			symbolChoice = self.getSymbolChoice()
			enemyChoice = 'O'
			if symbolChoice == 'X':
				enemyChoice = 'O'
			else:
				enemyChoice = 'X'
			gameRunning = True
			turn = 0
			gameAI = TicTacToeAI(enemyChoice)
			self.GameBoard.printBoard()
			while(not self.GameBoard.checkWin() and not self.GameBoard.checkFull()):
				if turn == 0:
					if symbolChoice == 'O' and players == 1:
						gameAI.botMove(self.GameBoard)
					else:
						self.makeMovePrompt('X')
					turn = 1
				else:
					if symbolChoice == 'X' and players == 1:
						gameAI.botMove(self.GameBoard)
					else:
						self.makeMovePrompt('O')
					turn = 0
				self.GameBoard.printBoard()
			if self.GameBoard.checkWin():
				if turn == 1:
					print("X wins!")
				else:
					print("O wins!")
			else:
				print("Game draw!")
			playAgain = self.getPlayAgainChoice()
			if playAgain == 'N':
				playing = False
			self.GameBoard = TicTacToeBoard()
			
			
	def makeMovePrompt(self, tac):
		valid = False
		while valid == False:
			try:
				position = int(input(tac + ", please select a position to place your tac."))
			except ValueError:
				print("Input is not an integer, please try again.")
				continue
			else:
				if(self.GameBoard.putTac(tac, position)):
					valid = True
				else:
					print("That move is entirely invalid. Please, try again: ")
				
		return position
	
	def getNumPlayers(self):
		print("Are there one or two players? Enter 1 for one player, or 2 for two players. \n")
		numPlayers = input()
		while(numPlayers != '1' and numPlayers != '2'):
			numPlayers = input("That is an altogether unacceptable number of players. Please try again: ")
		return int(numPlayers)
		
	def getSymbolChoice(self):
		print("Player one, please enter your choice of X or O. X goes first.\n")
		symbolChoice = input("").upper()
		while(symbolChoice != 'X' and symbolChoice != 'O'):
			symbolChoice = input("That is an altogether unacceptable choice. Please try again: ").upper()
		return symbolChoice
		
	def getPlayAgainChoice(self):
		print("Do you want to play again? Y/N")
		playAgain = input("").upper()
		while(playAgain != 'Y' and playAgain != 'N'):
			playAgain = input("That is an altogether unacceptable choice. Please try again: ").upper()
		return playAgain
		
TTTCLI = TicTacToeCLI()
TTTCLI.runGame()