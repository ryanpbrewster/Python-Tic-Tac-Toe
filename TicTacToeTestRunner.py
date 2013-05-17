""" This script is just used for running the pythontictactoe tests

The test suite is imported from the TicTacToeTests package

"""

import unittest
import pythontictactoe.TicTacToeTests.TicTacToeTests

loader = unittest.TestLoader()
suite = loader.loadTestsFromModule(pythontictactoe.TicTacToeTests.TicTacToeTests)

runner = unittest.TextTestRunner(verbosity = 2)
result = runner.run(suite)