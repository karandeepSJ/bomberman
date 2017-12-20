LIBRARIES USED
1. numpy       :      For easy 2-D array handling and for random.choice
2. os          :      For os.system("clear")
3. sys         :      For sys.stdin
4. getch       :      To take single character input
5. time        :      For time.sleep() function
6. termios     :      To flush output and input streams

USAGE
python3 game.py

SYMBOLS USED
Walls      :      X 
Bricks     :      / 
Bomberman  :      B(Green) 
Enemy      :      E(Red)
explosion  :      e(Yellow) 
Bombs      :      Timer(2->1->0) (blue) 

CONTROLS
w    :    Move Up
a    :    Move Left
s    :    Move Down
d    :    Move Right
b    :    Plant bomb at current location
q    :    Exit game

SCORING
Destroying brick   :   20 points
Killing enemy      :   100 points

DESCRIPTION:
Bomberman is an arcade-style maze-based game.

The player, Bomberman, must move around the maze while destroying his enemies with bombs. The maze is bound by indestructible walls. There are also some bricks that can be destroyed by bombs. The bomb will be planted at the location where the player was at the time of planting and will explode 3 frames later. The bomb will explode in the block it was planted in and to one neighbouring block on each of the four sides.

Your goal is to kill all the enemies while trying to stay alive. You will have 3 lives which you lose when you collide with an enemy or when you are within the explosion range. Killing all the enemies takes you to the next stage where you will face two more enemies than the previous stage. Your current lives will be increased by one when you advance to the next stage.

NOTES:
The game uses key presses as frames and not time. So, to go to the next frame, some key must be pressed. The enemies and bomb will also not progress automatically. If you want to wait at a particular location and want the game to progress, press any key except the ones defined above.

When the game is starting, the game title is displayed and stays for 3 seconds.

Whenever a new stage is about to start(including the first one), there is a three second pause where the stage number is displayed.

The explosion lasts 0.5 seconds during which all motor functions will be freezed.

HAVE FUN PLAYING :)
