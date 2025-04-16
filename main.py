# Braden Leach
# April 16 2025
# Pygame Text Menu


# -- Imports -- # 
import pygame 
import sys
import random 
import time

# -- Constants -- #
   # - Colors - # 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BROWN = (153, 76, 0)
PURPLE = (204, 0, 204)
ORANGE =  (255, 128, 0)
SKY_BLUE = (0, 255, 255)

   # - Widow - #
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

   # - Title - # 
TITLE = "Button Text Menu"

   # - Frame Rate - #
FPS = 60

    # - Text Font - # 
TEXT_FONT = "C:\\Project-Text-Menu\\DejaVuSans.ttf"

    # - Icon - #
ICON = "C:\\Project-Text-Menu\\favicon-starter-cropped.png"

    # - Sounds - #
rOBLOX_DEATH_SOUND = "C:\\Project-Text-Menu\\roblox-death-sound.ogg"
lAZER_SOUND = "C:\\Project-Text-Menu\\laser5.ogg"
zAP_SOUND = "C:\\Project-Text-Menu\\zap13.ogg"


# -- Load Sounds -- # 
roblox_soundL = pygame.mixer.Sound(rOBLOX_DEATH_SOUND)
lazer_soundL = pygame.mixer.Sound(lAZER_SOUND)
zap_soundL = pygame.mixer.Sound(zAP_SOUND)