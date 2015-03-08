""" This script is just used for running the pythontictactoe GUI

The GUI is imported from the TicTacToeGUI package

"""

from tkinter import *
from src.TicTacToeGUI import TicTacToeGUI

root = Tk()
root.wm_title("Play TicTacToe!")
TTT = TicTacToeGUI(root)
root.mainloop()
