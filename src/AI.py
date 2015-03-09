"""
A class containing all of the logic for an AI that plays TicTacToe

A note on the way the static and non-static methods work in this class:
* Static methods take a board, a tac to check, and a position, and return an
  evaluation (true or false). 
* Non-static methods, however, are called by an instance of the AI class. These
  methods are specifically used for making moves on a board which has been
  supplied. They're role is more than returning an evaluation: they change the
  state of the board which they are supplied with. 
* Basically, methods that are called by an instance of the class are proactive,
  i.e., they change the state of something. Class methods merely supply
  information.

"""
import math

class AI:
    def __init__(self, tac):
        """
        Initializes an AI instance with appropriate tacs. Should only be used
        if AI is going to play, not for making detections.
        """
        self.tac = tac
        self.enemy_tac = 'O' if tac == 'X' else 'X'

    def chooseMove(self, big_board):
        """
        Return (board_pos, pos), where board_pos is the position of the board
        you want to make a move in, and pos is the position within that board.

        If board_pos == None then it means you there is a free choice

        For now, the AI is dumb and just makes the first legal move it finds
        """

        board_pos = big_board.cur_board
        if board_pos == None:
            board_pos = big_board.legalBoards()[0]

        (i,j) = board_pos
        pos = big_board.boards[i][j].emptyPositions()[0]

        return board_pos, pos
