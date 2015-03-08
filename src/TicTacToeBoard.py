""" This class is used for storing the board in Tic Tac Toe Games

Methods in the class are used for printing the board, checking for wins and if the board is full,
and for placing tacs.

"""

import math

class TicTacToeBoard:
    def __init__(self):
        """ Initializes the board instance with an array of the digits 1 through 9 as characters. """
        self.TTTBoard = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    def printBoard(self):
        """ An instance method that prints out the board's current layout """
        for i in range(0,4,3):
            print(self.TTTBoard[i] + " | " + self.TTTBoard[i+1] + " | " + self.TTTBoard[i+2])
            print("--+---+--")
        print(self.TTTBoard[6] + " | " + self.TTTBoard[7] + " | " + self.TTTBoard[8] + "\n")

    def putTac(self, tac, pos):
        """ An instance method that puts a given tac at the given place in the board array if that position is not filled. """
        if int(pos) > 0 and int(pos) < 10:
            if(self.TTTBoard[int(pos)-1] == str(pos)):
                self.TTTBoard[int(pos)-1] = tac
                return True
            else:
                return False
        else:
            return False

    def checkWin(self):
        """ Instance methodchecking whether the board has a winner or not. Does not tell who the winner is."""
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
        """ Checks if all of the array elements have an X or O or not. """
        for i in self.TTTBoard:
            if i != 'X' and i != 'O':
                return False
        return True
