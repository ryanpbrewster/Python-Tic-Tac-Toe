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
from copy import deepcopy

class AI:
    WIN_REWARD = 100
    UNKNOWN_REWARD = 50
    LOSE_REWARD = 0


    def __init__(self, tac, level=1):
        """
        Initializes an AI instance with appropriate tacs. Should only be used
        if AI is going to play, not for making detections.
        """
        self.tac = tac
        self.enemy_tac = 'O' if tac == 'X' else 'X'
        self.level = level

    def chooseMove(self, large_board):
        """
        Return (board_pos, pos), where board_pos is the position of the board
        you want to make a move in, and pos is the position within that board.

        If board_pos == None then it means you there is a free choice

        For now, the AI is dumb and just makes the first legal move it finds
        """
        moves = self.allLegalMoves(large_board)
        scores = [ self.scoreMove(large_board, move) for move in moves ]
        best_move = max(zip(scores, moves))[1]
        return best_move


    def allMoves(self):
        return [ ((i,j), (ii,jj)) for i  in range(3) for j  in range(3)
                                  for ii in range(3) for jj in range(3) ]

    def allLegalMoves(self, large_board):
        return [ move for move in self.allMoves() if large_board.isLegalPlay(move) ]

    def firstLegalMove(self, large_board):
        return self.allLegalMoves(large_board)[0]

    def dumbScore(self, large_board):
        winner = large_board.winner()
        if winner == self.tac:
            return AI.WIN_REWARD
        elif winner == self.enemy_tac:
            return AI.LOSE_REWARD
        else:
            return AI.UNKNOWN_REWARD

    def scoreBoard(self, large_board):
        if self.level == 0:
            return self.dumbScore(large_board)

        lower_ai = AI(self.enemy_tac, self.level - 1)
        enemy_moves = lower_ai.allLegalMoves(large_board)
        if len(enemy_moves) == 0:
            return self.dumbScore(large_board)

        enemy_scores = [ lower_ai.scoreMove(large_board, move) for move in enemy_moves ]
        enemy_best_score = max(enemy_scores)

        return -enemy_best_score

    def scoreMove(self, large_board, move):
        copy_board = deepcopy(large_board)
        copy_board.putTac(self.tac, move)
        return self.scoreBoard(copy_board)
