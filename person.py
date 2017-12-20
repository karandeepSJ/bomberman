class Person():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.px = 0
        self.py = 0

    # Return coordinates of Person
    def get_coord(self):
        return self.x, self.y

    def move(self):
        pass

    def set_p(self):
        self.px = self.x
        self.py = self.y

    def get_p(self):
        return self.px, self.py
