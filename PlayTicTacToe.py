""" This script is just used for running the pythontictactoe GUI

The GUI is imported from the TicTacToeGUI package

"""

from tkinter import *
from src.GUI import GUI

root = Tk()
root.wm_title("Play TicTacToe!")
TTT = GUI(root)
root.mainloop()
