import numpy as np

# Functions in this file add the appropriate characters to the board matrix


# Function to make boundary walls
def make_boundaries(board):
    board[0:2, :] = 2 * [76 * ['X']]
    board[36:38, :] = 2 * [76 * ['X']]
    board[:, 0:4] = 38 * [4 * ['X']]
    board[:, 72:76] = 38 * [4 * ['X']]
    return board


# Function to make inner walls
def make_inner_wall(board):
    block = np.asarray([['X'] * 4] * 2)
    for i in range(4, 38, 4):
        for j in range(8, 68, 8):
            board[i:i + 2, j:j + 4] = block
    return board


# Function to move player in the matrix given his previous and
# present coordinates
def make_player(py, px, y, x, board):
    bomb_cond1 = (board[px][py] != '\033[94m2\033[0m' and
                  board[px][py] != '\033[94m1\033[0m' and
                  board[px][py] != '\033[94m0\033[0m' and
                  board[px][py] != '\033[94m0\033[0m')

    bomb_cond2 = (board[x][y] != '\033[94m2\033[0m' and
                  board[x][y] != '\033[94m1\033[0m' and
                  board[x][y] != '\033[94m0\033[0m' and
                  board[x][y] != '\033[94m0\033[0m')

    new_pos = np.asarray([['\033[92mB\033[0m'] * 4] * 2)
    prev_pos = np.asarray([[' '] * 4] * 2)
    if bomb_cond1 and board[px][py] != '\033[91mE\033[0m':
        board[px:px + 2, py:py + 4] = prev_pos
    if (board[x][y] != '\033[91mE\033[0m' and
            bomb_cond2 and board[x][y] != '\033[93me\033[0m'):
        board[x:x + 2, y:y + 4] = new_pos
    return board


# Function to place bricks
def make_brick(board, x, y):
    brick = np.asarray([['/'] * 4] * 2)
    board[x:x + 2, y:y + 4] = brick
    return board


# Function to move enenmy in the matrix given his previous and
# present coordinates
def make_enemy(board, py, px, y, x):
    bomb_cond1 = (board[px][py] != '\033[94m2\033[0m' and
                  board[px][py] != '\033[94m1\033[0m' and
                  board[px][py] != '\033[94m0\033[0m' and
                  board[px][py] != '\033[94m0\033[0m')

    bomb_cond2 = (board[x][y] != '\033[94m2\033[0m' and
                  board[x][y] != '\033[94m1\033[0m' and
                  board[x][y] != '\033[94m0\033[0m' and
                  board[x][y] != '\033[94m0\033[0m')

    prev_pos = np.asarray([[' '] * 4] * 2)
    enemy = np.asarray([['\033[91mE\033[0m'] * 4] * 2)
    if (bomb_cond1 and board[px][py] != '\033[93me\033[0m' and
            board[px][py] != '\033[92mB\033[0m'):
        board[px:px + 2, py:py + 4] = prev_pos
    if bomb_cond2 and board[x][y] != '\033[93me\033[0m':
        board[x:x + 2, y:y + 4] = enemy
    return board


# Function to place bomb
def make_bomb(board, y, x, time):
    bomb = np.asarray([['\033[94m' + str(time) + '\033[0m'] * 4] * 2)
    board[x:x + 2, y:y + 4] = bomb
    return board


# Function to make the explosion in matrix
def explode_bomb(board, y, x):
    bricks_broken = 0
    explosion = np.asarray([['\033[93me\033[0m'] * 4] * 2)
    board[x:x + 2, y:y + 4] = explosion
    if board[x][y - 1] == '/':
        bricks_broken += 1
    if board[x][y + 5] == '/':
        bricks_broken += 1
    if board[x - 1][y] == '/':
        bricks_broken += 1
    if board[x + 2][y] == '/':
        bricks_broken += 1

    if board[x][y - 1] != 'X':
        board[x:x + 2, y - 4:y] = explosion
    if board[x][y + 5] != 'X':
        board[x:x + 2, y + 4:y + 8] = explosion
    if board[x - 1][y] != 'X':
        board[x - 2:x, y:y + 4] = explosion
    if board[x + 2][y] != 'X':
        board[x + 2:x + 4, y:y + 4] = explosion
    return board, bricks_broken


# Function to clear the explosion from matrix
def clear_explosion(board, y, x):
    clear = np.asarray([[' '] * 4] * 2)
    board[x:x + 2, y:y + 4] = clear
    if board[x][y - 1] == '\033[93me\033[0m':
        board[x:x + 2, y - 4:y] = clear
    if board[x][y + 5] == '\033[93me\033[0m':
        board[x:x + 2, y + 4:y + 8] = clear
    if board[x - 1][y] == '\033[93me\033[0m':
        board[x - 2:x, y:y + 4] = clear
    if board[x + 2][y] == '\033[93me\033[0m':
        board[x + 2:x + 4, y:y + 4] = clear
    return board
