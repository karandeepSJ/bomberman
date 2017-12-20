import numpy as np


class Board():

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board = np.asarray([[' '] * cols] * rows)
        # convert board to dtype <U11 to store colored characters
        self.board = self.board.astype(dtype='<U11')

    def get_board(self):
        return self.board
