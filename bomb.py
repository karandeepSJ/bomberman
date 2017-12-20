class Bomb():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.timeleft = 3

    def dec_time(self):
        self.timeleft -= 1

    def get_coord(self):
        return self.x, self.y

    def get_time_left(self):
        return self.timeleft
