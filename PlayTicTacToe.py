""" This script is just used for running the pythontictactoe GUI

The GUI is imported from the TicTacToeGUI package

"""

from tkinter import *
from pythontictactoe.TicTacToeInterfaces.TicTacToeGUI import TTTGame

root = Tk()
root.wm_title("Play TicTacToe!")
TTT = TTTGame(root)
root.mainloop()
