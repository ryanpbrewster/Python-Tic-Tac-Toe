from TicTacToe import *

print("Welcome to Tic Tac Toe! \n");
playing = True
board = TicTacToeBoard()

while(playing):
## This is just setting up the game (number of players, player symbols, et cetera)
	print("Are there one or two players? Enter 1 for one player, or 2 for two players. \n")
	numPlayers = int(input())
	while(numPlayers != 1 and numPlayers != 2):
		numPlayers = input("That is an altogether unacceptable number of players. Please try again: ")
	print("Player one, please enter your choice of X or O. X goes first.\n")
	symbolChoice = input("").upper()
	while(symbolChoice != 'X' and symbolChoice != 'O'):
		symbolChoice = input("That is an altogether unacceptable choice. Please try again: ")
	
	
	turn = 1
	board.printBoard()
	while(not board.checkWin() and not board.checkFull()):
		if turn == 1:
			if symbolChoice == 'X':
				board.makeMovePrompt('X')
			else:
				board.botMove('X')
			turn = 0
		else:
			if numPlayers == 2:
				board.makeMovePrompt('O')
			else:
				if symbolChoice == 'X':
					board.botMove('O')
				else:
					board.makeMovePrompt('O')
			turn = 1
		board.printBoard()
	if board.checkWin():
		if turn == 1:
			print("O wins!")
		else:
			print("X wins!")
	else:
		print("Game draw!")
	playing = False
	