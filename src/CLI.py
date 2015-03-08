"""
This module is used for running a command line interface version of the tic tac
toe game

Because the CLI imports TicTacToeBoard and TicTacToeAI, it has to be run from
an external script which instantiates the CLI.
"""

from src.LargeBoard import LargeBoard
from src.SmallBoard import SmallBoard
from src.AI import AI

class CLI:
    def __init__(self):
        self.big_board = LargeBoard()

    def runGame(self):
        playing = True
        while playing:
            players = self.getNumberOfPlayers()
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
        """ Method used for prompting for a move from either player """
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
        """ Method used for prompting for the number of players """
        print("Are there one or two players? Enter 1 for one player, or 2 for two players. \n")
        numPlayers = raw_input()
        while numPlayers not in "12":
            numPlayers = raw_input("That is an altogether unacceptable number of players. Please try again: ")
        return int(numPlayers)
        
    def getSymbolChoice(self):
        """ Method used for prompting for player one's choice of tac """
        print("Player one, please enter your choice of X or O. X goes first.\n")
        symbolChoice = raw_input("").upper()
        while(symbolChoice != 'X' and symbolChoice != 'O'):
            symbolChoice = raw_input("That is an altogether unacceptable choice. Please try again: ").upper()
        return symbolChoice
        
    def getPlayAgainChoice(self):
        """ Method used for prompting for whether or not the player or players will play again. """
        print("Do you want to play again? Y/N")
        playAgain = raw_input("").upper()
        while(playAgain != 'Y' and playAgain != 'N'):
            playAgain = raw_input("That is an altogether unacceptable choice. Please try again: ").upper()
        return playAgain
        
