TILESIZE = 32  # Tile size in pixels

# Game field(grid) size in tiles
GRIDWIDTH = 10
GRIDHEIGHT = 20

FIELDWIDTH = GRIDWIDTH * TILESIZE  # Game window width in pixels
FIELDHEIGHT = GRIDHEIGHT * TILESIZE  # Game window height in pixels

WINDOWWIDTH = 640
WINDOWHEIGHT = 800

FPS = 60  # game speed is fixed to 60 frames per second

FALLINGSPEED = 0.001     # figure falling speed in plying field's cell per millisecond (cell/ms)
SPEED_INCREMENT = 0.0005  # speed increment for level progression
SPEEDMULTIPLIER = 20  # accelerated figure falling speed (cell/ms)

STARTING_POSITION = (4, 0)  # figure spawn position

background = "resources/background.png"

# Network constants

# Theodore
IPV4 = '25.47.240.219'  # cmd> ipconfig
# Denis
# IPV4 = '25.50.55.253'
# Valentin
# IPV4 = '25.48.128.45'
PORT = 5555
PACKAGE_SIZE = 4096
