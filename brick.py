import numpy as np


class Brick():

    def __init__(self):
        self.x = 0
        self.y = 0

    # Choose a random position for enemy and set coordinates there
    def place_brick(self, possibility):
        ind = np.random.choice(len(possibility))
        coord = possibility[ind]
        possibility = possibility.tolist()
        possibility.pop(ind)
        self.x = coord[0]
        self.y = coord[1]
        return possibility

    def get_coord(self):
        return self.x, self.y
