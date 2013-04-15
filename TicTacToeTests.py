import unittest
from TicTacToe import *

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
		self.assertTrue(testBoard.isWinningMove('X', 3))
		self.assertFalse(testBoard.isWinningMove('X', 8))
		
	def test_makesFork(self):
		testBoard = TicTacToeBoard()
		testBoard.putTac('X', 2)
		testBoard.putTac('X', 4)
		self.assertTrue(testBoard.makesFork('X', 1))
	
	def test_botMove(self):
		testBoard = TicTacToeBoard()
		testBoard.putTac('X', 1)
		testBoard.putTac('X', 2)
		# Tests that AI, seeing no win for itself, blocks potential enemy win
		testBoard.botMove('O')
		self.assertEqual(testBoard.TTTBoard[2], 'O')
		testBoard.putTac('O', 6)
		# Tests that AI, seeing a win for itself, takes it
		testBoard.botMove('O')
		self.assertEqual(testBoard.TTTBoard[8], 'O')
		
		testBoard = TicTacToeBoard()
		testBoard.putTac('X',2)
		testBoard.putTac('X',4)
		# Tests that AI, seeing a potential fork, prevents it
		testBoard.botMove('O')
		self.assertEqual(testBoard.TTTBoard[0], 'O')
		
		testBoard = TicTacToeBoard()
		# Tests that AI goes for center if it has no winning position, fork, or anything to prevent
		testBoard.botMove('O')
		self.assertEqual(testBoard.TTTBoard[4], 'O')
	def test_makesTwoInARow(self):
		testBoard = TicTacToeBoard()
		testBoard.putTac('X', 2)
		self.assertTrue(testBoard.makesTwoInARow('X', 3))
unittest.main()