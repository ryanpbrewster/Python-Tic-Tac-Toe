"""
This class is used for storing the board in Tic Tac Toe Games

Methods in the class are used for checking for wins, if the board is full, and
for placing tacs.
"""

import math
from src.Util import transpose

class SmallBoard:
    def __init__(self):
        """
        Initializes an empty board (3x3 array of cells)
        """
        self.board = [ ['.', '.', '.']
                     , ['.', '.', '.']
                     , ['.', '.', '.']
                     ]

    def __repr__(self):
        return "".join(self.board[i][j] for i in range(3) for j in range(3))

    def isPositionEmpty(self, pos):
        """
        Is the cell in the given position empty?
        """
        i, j = pos
        assert 0 <= i <= 2 and 0 <= j <= 2
        return self.board[i][j] not in "XO"

    def putTac(self, tac, pos):
        """
        An instance method that puts a given tac at the given place in the
        board array if that position is not filled.
        """
        i, j = pos
        assert 0 <= i <= 2 and 0 <= j <= 2
        assert self.board[i][j] not in "XO"
        self.board[i][j] = tac

    def winner(self):
        """
        Determines who won.
        If no one won, returns None
        """
        rows = self.board
        cols = transpose(self.board)
        diags = [ [self.board[0][0], self.board[1][1], self.board[2][2]] \
                , [self.board[2][0], self.board[1][1], self.board[0][2]] ]
        for trip in rows+cols+diags:
            if trip[0] in "XO" and trip[0] == trip[1] == trip[2]:
                return trip[0]
        return None

    def hasWinner(self):
        """
        Instance methodchecking whether the board has a winner or not. Does not
        tell who the winner is.
        """
        return self.winner() != None


    def isFull(self):
        """
        Is the small board full?
        """
        for i in range(3):
            for j in range(3):
                if self.board[i][j] not in "XO":
                    return False
        return True

    def isLegal(self):
        return not self.isFull() and not self.hasWinner()

    def emptyPositions(self):
        return [(i,j) for i in range(3) for j in range(3) if self.board[i][j] not in "XO"]
