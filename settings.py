# Pygame Settings
# Tony Mildon
# Start Date - 19/05/2020

import pygame as pg
vec = pg.math.Vector2

# define some colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BROWN = (106, 55, 5)
CYAN = (0, 255, 255)

# game settings
WIDTH = 1200   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 600  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
TITLE = "Tilemap Demo"
BGCOLOR = BROWN

TILESIZE = 64
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

WALL_IMG = 'wall_sprite.png'

# Player settings
PLAYER_HEALTH = 100
PLAYER_SPEED = 200
PLAYER_ROT_SPEED = 250
PLAYER_IMG = 'sprite_new.png'
PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35)
BARREL_OFFSET = vec(30, 10)

# Gun settings
BULLET_IMG = 'bullet_sprite2.png'
BULLET_SPEED = 800
BULLET_LIFETIME = 1000
BULLET_RATE = 75
KICKBACK = 150
GUN_SPREAD = 20
BULLET_DAMAGE = 20

# Mob settings
MOB_IMG = 'mob_new.png'
MOB_SPEEDS = [350, 300, 200, 225]
MOB_HIT_RECT = pg.Rect(0, 0, 30, 30)
MOB_HEALTH = 100
MOB_DAMAGE = 20
MOB_KNOCKBACK = 5
AVOID_RADIUS = 50
DETECT_RADIUS = 600

# Effects
MUZZLE_FLASHES = ['flash.png', 'flash2.png', 'flash3.png']

FLASH_DURATION = 30

# Layers
WALL_LAYER = 1
PLAYER_LAYER = 2
BULLET_LAYER = 3
MOB_LAYER = 2
EFFECTS_LAYER = 4
