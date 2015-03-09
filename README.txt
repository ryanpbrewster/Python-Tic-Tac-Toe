A Python implementation of 9-board tic tac toe.

The rules are as follows:
    The gamespace is divided into 9 boards (i.e., SmallBoard)
    Each board has 9 spaces in it
    A ``move'' involves putting a mark in a space
    The space that is marked dictates which board must be used for the next player
        That is, suppose player 1 places a mark in the upper left space of a board
        Player 2 must then make a move in the upper left board (there is no constraint on which space they choose):w

    The first player may make a move whever they desire

    When a board is ``won'' (according to standard tic-tac-toe rules), it is no longer active

    A player wins the game when they achieve a standard tic-tac-toe victory using won boards
