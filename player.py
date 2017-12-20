from person import Person


class Player(Person):

    # Move the Bomberman according to the direction specified by player
    def move(self, key, board):
        if key == 'a':
            if (self.x > 4 and
                (board[self.y][self.x - 4] == ' ' or
                 board[self.y][self.x - 4] == '\033[91mE\033[0m' or
                 board[self.y][self.x - 4] == '\033[93me\033[0m')):
                self.x -= 4
        elif (key == 'd' and
              (board[self.y][self.x + 4] == ' ' or
               board[self.y][self.x + 4] == '\033[91mE\033[0m' or
               board[self.y][self.x + 4] == '\033[93me\033[0m')):
            if self.x < 68:
                self.x += 4
        elif (key == 'w' and
              (board[self.y - 2][self.x] == ' ' or
               board[self.y - 2][self.x] == '\033[91mE\033[0m' or
               board[self.y - 2][self.x] == '\033[93me\033[0m')):
            if self.y > 2:
                self.y -= 2
        elif (key == 's' and
              (board[self.y + 2][self.x] == ' ' or
               board[self.y + 2][self.x] == '\033[91mE\033[0m' or
               board[self.y + 2][self.x] == '\033[93me\033[0m')):
            if self.y < 34:
                self.y += 2
