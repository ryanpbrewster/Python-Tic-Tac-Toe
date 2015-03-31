"""
This class is used for storing the board in Tic Tac Toe Games

Methods in the class are used for printing the board, checking for wins and if
the board is full, and for placing tacs.
"""

import math
from src.Util import transpose
from src.SmallBoard import SmallBoard

class LargeBoard:
    PLAYER_TAC_MAP = { 0 : "X", 1 : "O" }
    def __init__(self):
        """
        Initializes an 3x3 array of empty SmallBoards
        """
        self.boards = [[ SmallBoard() for j in range(3) ] for i in range(3) ]
        self.cur_board = None
        self.active_player = 0

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

    def nextPlayer(self):
        if self.active_player == 0:
            return 1
        else:
            return 0

    def switchActivePlayer(self):
        self.active_player = self.nextPlayer()

    def putTac(self, tac, board_pos, pos):
        """
        Place `tac` in board (i,j) at position `pos`
        Fails if `tac` is 
        """
        assert tac == LargeBoard.PLAYER_TAC_MAP[self.active_player]

        i, j = board_pos
        assert 0 <= i <= 2 and 0 <= j <= 2

        assert self.isLegalPlay(board_pos, pos)

        self.boards[i][j].putTac(tac, pos)
        if self.getBoard(pos).isLegal():
            self.cur_board = pos
        else:
            self.cur_board = None
        self.switchActivePlayer()
        print("Placed %s at (%d,%d) in board (%d,%d)"%(tac, pos[0], pos[1], i, j))

    def playerMove(self, board_pos, pos):
        active_tac = LargeBoard.PLAYER_TAC_MAP[self.active_player]
        self.putTac(active_tac, board_pos, pos)

    def winner(self):
        """
        Figures out who the winner of this instance is. If there is no winner,
        returns None
        """
        rows = self.boards
        cols = transpose(self.boards)
        diags = [ [self.boards[0][0], self.boards[1][1], self.boards[2][2]] \
                , [self.boards[2][0], self.boards[1][1], self.boards[0][2]] ]
        for bs in rows+cols+diags:
            if all(b.hasWinner() for b in bs) and bs[0].winner() == bs[1].winner() == bs[2].winner():
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

    def isActive(self, board_pos):
        """
        Is the board at board_pos active (that is, can you legally make a move
        there?)
        """
        i, j = board_pos
        if not self.boards[i][j].isLegal():
            return False
        if self.cur_board == None or self.cur_board == board_pos:
            return True
        return False

    def legalBoards(self):
        return [ (i,j) for i in range(3) for j in range(3) if self.boards[i][j].isLegal() ]
