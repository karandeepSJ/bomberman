import numpy as np
from person import Person


class Enemy(Person):

    # Choose a random position for enemy and set coordinates there
    def spawn(self, possibility):
        ind = np.random.choice(len(possibility))
        coord = possibility[ind]
        possibility = possibility.tolist()
        possibility.pop(ind)
        self.y = coord[0]
        self.x = coord[1]
        self.px = self.x
        self.py = self.y
        return possibility

    # Move the enemy
    def move(self, key):
        if key == 'a':
            self.x -= 4
        elif key == 'd':
            self.x += 4
        elif key == 'w':
            self.y -= 2
        elif key == 's':
            self.y += 2

    # Select a random direction for enemy to move
    def select_dir(self, board):
        keys = []
        if (self.x > 4 and
            (board[self.y][self.x - 4] == ' ' or
             board[self.y][self.x - 4] == '\033[92mB\033[0m' or
             board[self.y][self.x - 4] == '\033[93me\033[0m')):
            keys.append('a')
        if (self.x < 68 and
            (board[self.y][self.x + 4] == ' ' or
             board[self.y][self.x + 4] == '\033[92mB\033[0m' or
             board[self.y][self.x + 4] == '\033[93me\033[0m')):
            keys.append('d')
        if (self.y > 2 and
            (board[self.y - 2][self.x] == ' ' or
             board[self.y - 2][self.x] == '\033[92mB\033[0m' or
             board[self.y - 2][self.x] == '\033[93me\033[0m')):
            keys.append('w')
        if (self.y < 34 and
            (board[self.y + 2][self.x] == ' ' or
             board[self.y + 2][self.x] == '\033[92mB\033[0m' or
             board[self.y + 2][self.x] == '\033[93me\033[0m')):
            keys.append('s')
        if(len(keys) != 0):
            self.move(keys[np.random.choice(len(keys))])
