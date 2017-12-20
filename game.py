import numpy as np
import render
from player import Player
from brick import Brick
from board import Board
from bomb import Bomb
from enemy import Enemy
import os
import getch
import time
import sys
from termios import tcflush, TCIFLUSH


class Game():

    score = 0
    lives = 3

    def __init__(self, enemies, bricks):
        self.complete = False
        self.key = 'v'
        self.dead = False
        self.bomb = None
        self.no_enemies = enemies
        self.empty = []
        self.no_bricks = bricks

    def __reinit(self):
        self.complete = False
        self.key = 'v'
        self.dead = False
        self.bomb = None
        self.no_enemies = self.no_enemies
        self.no_bricks = self.no_bricks
        self.empty = []

    def __dec_lives(self):
        Game.lives -= 1

    def inc_lives(self):
        Game.lives += 1
    # Make a list containing all the black blocks on the board after walls
    # are created. These blank blocks will be used to add enemies and
    # bricks randomly

    def __make_poss_array(self):
        for i in range(2, 36, 2):
            if i % 4 != 0:
                for j in range(4, 72, 4):
                    self.empty.append([i, j])
            else:
                for j in range(4, 72, 8):
                    self.empty.append([i, j])
        self.empty.pop(0)

    def __add_bricks(self):
        self.__make_poss_array()
        for i in range(self.no_bricks):
            brick = Brick()
            self.empty = brick.place_brick(np.asarray(self.empty))
            x, y = brick.get_coord()
            self.board = render.make_brick(self.board, x, y)

    def __initialize_game(self):
        # make board object
        b = Board(38, 76)
        self.board = b.get_board()

        # Make walls
        self.board = render.make_boundaries(self.board)
        self.board = render.make_inner_wall(self.board)

        # Make Bricks
        self.__add_bricks()

        # Make Bomberman
        self.p = Player(4, 2)
        x, y = self.p.get_coord()
        self.p.set_p()
        px, py = self.p.get_p()
        self.board = render.make_player(px, py, x, y, self.board)

        # Make enemies
        self.enemies = []
        for i in range(self.no_enemies):
            e = Enemy(0, 0)
            self.empty = e.spawn(np.asarray(self.empty))
            self.enemies.append(e)
            e1, e2 = e.get_coord()
            pe1 = e1
            pe2 = e2
            self.board = render.make_enemy(self.board, pe1, pe2, e1, e2)

    # Print the board along with score and lives left
    def __display(self):
        for i in self.board:
            print(''.join(i))
        print("Score: " + str(Game.score) +
              "                                       " + "Lives left: " +
              str(Game.lives - 1))

    # Display explosion, sleep for 0.5 seconds to show,
    # then clear the explosion and display again
    def __make_and_clear_explosion(self, r, c):
        os.system('clear')
        self.__display()
        time.sleep(0.5)
        tcflush(sys.stdin, TCIFLUSH)
        render.clear_explosion(self.board, r, c)
        self.bomb = None
        os.system('clear')
        self.__display()

    def __check_person_death_by_bomb(self, x, y, r, c):
        if (((y == c) and (x == r - 4 or x == r + 4)) or
                ((x == r) and (y == c - 2 or y == c + 2)) or
                (x == r and y == c)):
            return True
        else:
            return False

    def __check_player_death_by_enemy(self, x, y, e1, e2):
        if (x == e1 and y == e2):
            return True
        else:
            return False

    def __disp_score(self):
        print("SCORE: %d".center(os.get_terminal_size().columns) % Game.score)

    def __death_message(self):
        print("")
        print("DEAD!! You lost a life.".center(os.get_terminal_size().columns))
        self.__disp_score()
        print("Press any key to continue".center(
            os.get_terminal_size().columns))

    def __kill_bomberman(self):
        os.system('clear')
        self.__display()
        self.__death_message()
        getch.getch()

    def __play_game(self):
        os.system('clear')
        self.__display()
        while self.key != 'q':
            x, y = self.p.get_coord()
            if self.bomb:                          # If bomb has been planted
                if self.bomb.get_time_left() > 0:
                    self.bomb.dec_time()
                    disp_time = self.bomb.get_time_left() - 1
                    if(self.bomb.get_time_left() == 0):
                        disp_time += 1
                    bx, by = self.bomb.get_coord()
                    self.board = render.make_bomb(
                        self.board, bx, by, disp_time)
                elif self.bomb.get_time_left() == 0:
                    r, c = self.bomb.get_coord()
                    self.board, bricks_des = render.explode_bomb(
                        self.board, r, c)
                    Game.score += (bricks_des * 20)
                    if(self.__check_person_death_by_bomb(x, y, r, c)):
                        self.__make_and_clear_explosion(r, c)
                        self.__kill_bomberman()
                        break

                    # remove the enemies killed by explosion from
                    # the enemies list
                    enn = []
                    for i in range(len(self.enemies)):
                        e1, e2 = self.enemies[i].get_coord()
                        if(self.__check_person_death_by_bomb(e1, e2, r, c)):
                            Game.score += 100
                        else:
                            enn.append(self.enemies[i])
                    self.enemies = enn
                    # If all enemies dead
                    if(self.enemies == []):
                        os.system('clear')
                        self.__display()
                        print("You Won!!".center(
                            os.get_terminal_size().columns))
                        self.__disp_score()
                        self.complete = True
                        break
                    self.__make_and_clear_explosion(r, c)

            self.key = getch.getch()
            if self.key != 'b':
                self.p.move(self.key, self.board)
                x, y = self.p.get_coord()
                px, py = self.p.get_p()
                self.board = render.make_player(px, py, x, y, self.board)

            # If 'b' is pressed and a bomb is not already planted
            elif self.bomb is None:
                self.bomb = Bomb(x, y)
                self.board = render.make_bomb(
                    self.board, x, y, self.bomb.get_time_left() - 1)
            # After player moves, check if he lands on an enemy
            # If yes, kill the bomberman
            for g in range(len(self.enemies)):
                e = self.enemies[g]
                e1, e2 = e.get_coord()
                if(self.__check_player_death_by_enemy(x, y, e1, e2)):
                    self.dead = True
                    self.__kill_bomberman()
                    break
            if self.dead is True:
                break
            # Move enemy and check if player dies
            for g in range(len(self.enemies)):
                e = self.enemies[g]
                e.select_dir(self.board)
                e1, e2 = e.get_coord()
                pe1, pe2 = e.get_p()
                self.board = render.make_enemy(self.board, pe1, pe2, e1, e2)
                if(self.__check_player_death_by_enemy(x, y, e1, e2)):
                    self.dead = True
                    self.__kill_bomberman()
                    break

            if self.dead is True:
                break
            os.system('clear')
            self.__display()
            sys.stdout.flush()
            self.p.set_p()
            for i in range(len(self.enemies)):
                self.enemies[i].set_p()

    def start(self):
        while(Game.lives):
            self.__initialize_game()
            self.__play_game()
            if self.complete:
                return True
            if self.key == 'q':
                break
            self.__dec_lives()
            self.__reinit()
        print("")
        print("GAME OVER.".center(os.get_terminal_size().columns))
        self.__disp_score()
        return False


cols = os.get_terminal_size().columns
lines = os.get_terminal_size().lines
os.system("clear")
for i in range(lines // 2):
    print("")
print("\033[1mB   O   M   B   E   R   M   A   N\033[0m".center(cols))
tcflush(sys.stdin, TCIFLUSH)
enemies = 3
bricks = 20
a = True
stage = 1
while a:
    time.sleep(3)
    tcflush(sys.stdin, TCIFLUSH)
    os.system("clear")
    for i in range(lines // 2):
        print("")
    print("S T A G E :   %d".center(os.get_terminal_size().columns) % stage)
    time.sleep(3)
    tcflush(sys.stdin, TCIFLUSH)
    game = Game(enemies, bricks)
    a = game.start()
    enemies += 2
    bricks += 5
    stage += 1
    game.inc_lives()
