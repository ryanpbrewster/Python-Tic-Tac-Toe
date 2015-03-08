"""
This class is used for storing the board in Tic Tac Toe Games

Methods in the class are used for printing the board, checking for wins and if
the board is full, and for placing tacs.
"""

import math
from src.Util import transpose
from src.SmallBoard import SmallBoard

class LargeBoard:
    def __init__(self):
        """
        Initializes an 3x3 array of empty SmallBoards
        """
        self.boards = [[ SmallBoard() for j in range(3) ] for i in range(3) ]
        self.cur_board = None

    def getBoard(self, pos):
        return self.boards[pos[0]][pos[1]]

    def __repr__(self):
        return "\n".join("(%d,%d) -> %s"%(i,j, str(self.boards[i][j]))
                             for i in range(3) for j in range(3) )

    def isLegalPlay(self, board_pos, cell_pos):
        """
        Is it legal to place a tac at the given board_pos and cell_pos?
        """
        i, j = board_pos
        assert 0 <= i <= 2 and 0 <= j <= 2

        # Make sure the play is in the active board
        # Recall that self.cur_board == None indicates that all boards are active
        if self.cur_board != None and board_pos != self.cur_board:
            return False

        # Make sure the desired board isn't already won
        if self.boards[i][j].hasWinner():
            return False

        # Lastly, make sure the spot in that board is open
        return self.boards[i][j].isPositionEmpty(cell_pos)

    def putTac(self, tac, board_pos, pos):
        """
        Place `tac` in board (i,j) at position `pos`
        """
        i, j = board_pos
        assert 0 <= i <= 2 and 0 <= j <= 2

        self.boards[i][j].putTac(tac, pos)
        if self.getBoard(pos).isLegal():
            self.cur_board = pos
        else:
            self.cur_board = None
        print("Placed %s at (%d,%d) in board (%d,%d)"%(tac, pos[0], pos[1], i, j))
        print(self)

    def winner(self):
        """
        Instance methodchecking whether the board has a winner or not. Does not
        tell who the winner is.
        """
        rows = self.boards
        cols = transpose(self.boards)
        diags = [ [self.boards[0][0], self.boards[1][1], self.boards[2][2]] \
                , [self.boards[2][0], self.boards[1][1], self.boards[0][2]] ]
        for bs in rows+cols+diags:
            if all(b.hasWinner() for b in bs) and bs[0].winner() == bs[1].winner() == bs[2].winner():
                print("Found a winner")
                print(bs[0].winner() + bs[1].winner() + bs[2].winner())
                return bs[0].winner()
        return None

    def hasWinner(self):
        """
        Is the game over?
        """
        return self.winner() != None

    def isFull(self):
        """
        Is every single board full?
        """
        return all(self.boards[i][j].isFull() for i in range(3) for j in range(3))

    def nonfullBoards(self):
        return [ (i,j) for i in range(3) for j in range(3) if not self.boards[i][j].isFull() ]