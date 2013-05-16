import unittest
from TicTacToeAI import *
from TicTacToeBoard import *

class TestTicTacToeBoard(unittest.TestCase):
	def test_CheckWin(self):
		testBoard = TicTacToeBoard()
		testBoard.putTac('X',1)
		testBoard.putTac('O',4)
		testBoard.putTac('X',2)
		testBoard.putTac('O',5)
		testBoard.putTac('X',3)
		self.assertTrue(testBoard.checkWin())
		testBoard = TicTacToeBoard()
		testBoard.putTac('X',1)
		testBoard.putTac('O',4)
		testBoard.putTac('X',5)
		testBoard.putTac('O',7)
		testBoard.putTac('X',9)
		self.assertTrue(testBoard.checkWin())
		
	def test_PutTac(self):
		testBoard = TicTacToeBoard()
		testBoard.putTac('X',1)
		self.assertEqual(testBoard.TTTBoard[0], 'X')
		
	def test_CheckFull(self):
		testBoard = TicTacToeBoard()
		for i in range(1, 10):
			testBoard.putTac('X', i)
		self.assertTrue(testBoard.checkFull())
		testBoard = TicTacToeBoard()
		self.assertFalse(testBoard.checkFull())
		
	def test_isWinningMove(self):
		testBoard = TicTacToeBoard()
		testBoard.putTac('X', 1)
		testBoard.putTac('X', 2)
		self.assertTrue(TicTacToeAI.isWinningMove('X', testBoard, 3))
		self.assertFalse(TicTacToeAI.isWinningMove('X', testBoard, 8))
		
	def test_makesTwoInARow(self):
		testBoard = TicTacToeBoard()
		testBoard.putTac('X', 2)
		self.assertTrue(TicTacToeAI.makesTwoInARow('X', testBoard, 3))
		
	def test_makesFork(self):
		testBoard = TicTacToeBoard()
		testBoard.putTac('X', 2)
		testBoard.putTac('X', 4)
		self.assertTrue(TicTacToeAI.makesFork(testBoard, 'X', 1))
		self.assertFalse(TicTacToeAI.makesFork(testBoard, 'O', 1))
	
	
	def test_botMovePreventFork(self):
		# Should lay down a tac to prevent an enemy fork
		testBoard = TicTacToeBoard()
		testAI = TicTacToeAI('O')
		testBoard.putTac('X', 6)
		testBoard.putTac('X', 8)
		testAI.botMove(testBoard)
		self.assertTrue(testBoard.TTTBoard[8], 'O')
		
		# Should create two tacs in a row to force enemy to block
		testBoard = TicTacToeBoard()
		testBoard.putTac('X', 1)
		testBoard.putTac('X', 9)
		testBoard.putTac('O', 5)
		testAI.botMove(testBoard)
		self.assertTrue(testBoard.TTTBoard[1], 'O')
		
	
	def test_botMovePreventWin(self):
		testBoard = TicTacToeBoard()
		testAI = TicTacToeAI('O')
		testBoard.putTac('X', 1)
		testBoard.putTac('X', 2)
		testAI.botMove(testBoard)
		self.assertTrue(testBoard.TTTBoard[2], 'O')
		
		testBoard = TicTacToeBoard()
		testBoard.putTac('X', 1)
		testBoard.putTac('X', 5)
		testAI.botMove(testBoard)
		self.assertTrue(testBoard.TTTBoard[8], 'O')
	
	
	def test_botMoveWin(self):
		testBoard = TicTacToeBoard()
		testAI = TicTacToeAI('O')
		testBoard.putTac('O', 1)
		testBoard.putTac('O', 2)
		testAI.botMove(testBoard)
		self.assertTrue(testBoard.TTTBoard[2], 'O')
		
		testBoard = TicTacToeBoard()
		testBoard.putTac('O', 1)
		testBoard.putTac('O', 5)
		testAI.botMove(testBoard)
		self.assertTrue(testBoard.TTTBoard[8], 'O')
		
	def test_botMoveTakeCenter(self):
		testBoard = TicTacToeBoard()
		testAI = TicTacToeAI('O')
		testAI.botMove(testBoard)
		self.assertTrue(testBoard.TTTBoard[4], 'O')
		
		testBoard = TicTacToeBoard()
		testBoard.putTac('X', 1)
		testAI.botMove(testBoard)
		self.assertTrue(testBoard.TTTBoard[4], 'O')
		
	def test_botMoveTakeOppositeCorner(self):
		testBoard = TicTacToeBoard()
		testAI = TicTacToeAI('O')
		testBoard.putTac('X', 1)
		testBoard.putTac('O', 5)
		testAI.botMove(testBoard)
		self.assertTrue(testBoard.TTTBoard[8], 'O')
		
		
unittest.main()