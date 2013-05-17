Python Tic-Tac-Toe:
- Only compatible with PYTHON 3

Installing Python 3:
	* For windows users, download and run the installer for Python 3.3.2 or higher at http://python.org/download/
	* For Linux users, check the python.org website or your distros website. For debian and ubuntu users, the command "sudo apt-get install python3.3" may work.
	* For OS X users, download and run the installer for Python 3.3.2 or higher at http://www.python.org/download/

File overview:
	TicTacBoard.py: Contains all of the logic for the TicTacToe board, including putting down tacs and checking for wins
	TicTacToeAI.py: Contains all of the logic for the TicTacToeAI, including bot movement and detection of forks and wins.
	TicTacToeGUI.py: Contains all of the code for a Tkinter GUI for TicTacToe
	TicTacToeCLI.py: Contains all of the code for a Command Line Interface for TicTacToe
	TicTacToeTests.py: Unit test suite for TicTacToeAI.py and TicTacToeBoard.py logic
	PlayTicTacToe.py: Runnable file for launching the TicTacToe GUI
	PlayTicTacToeCLI.py: Runnable file for launching the TicTacToe CLI
	TicTacToeTestRunner.py: Runnable file for running the TicTacToe test suite

Reading and modifying code:
	* All code is documented according to PEP 8 and PEP 257
	* Packages are separated accordingly: Logic layer, Interface layer, Test layer

To run:
	* Run PlayTicTacToe.py using PYTHON 3
		- This is the primary way of playing the game.
		- To run, navigate to the folder containing PlayTicTacToe.py using the command line or terminal, then type "python PlayTicTacToe.py"
	* Alternatively, run PlayTicTacToeCLI.py using PYTHON 3
		- This is primarily used for testing, not recommended

To test:
	* Run the TicTacToeTestRunner.py file using Python 3
