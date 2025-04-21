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
ROBLOX_DEATH_SOUND = "C:\\Project-Text-Menu\\roblox-death-sound.ogg"
LAZER_SOUND = "C:\\Project-Text-Menu\\laser5.ogg"


# -- Intilize -- # 
def init_game (): 
    pygame.init()
    pygame.font.init()
    pygame.mixer.init()  # Initialize the mixer
    pygame.mixer.music.load("C:\Project-Text-Menu\epic-skies-SBA-348586748-preview.mp3") # Load Music
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) # Use constants from config
    pygame.display.set_caption(TITLE)
    return screen


# -- Events -- # 
def handle_events ():
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
          return False
       elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
             return False
    return True


# -- Draw Text -- # 
def draw_text(screen, text, font, text_color, y, bold=False, italic = False): 
   font.set_bold(bold)
   font.set_italic(italic)

   text_surface = font.render(text, True, text_color)
   screen.blit(text_surface, (90, y))


def main():
   screen = init_game()
   clock = pygame.time.Clock() # Initialize the clock here

   # -- Load Sounds -- # 
   roblox_soundL = pygame.mixer.Sound(ROBLOX_DEATH_SOUND)
   lazer_soundL = pygame.mixer.Sound(LAZER_SOUND)


   # -- Font -- # 
   text_font = pygame.font.Font(TEXT_FONT, 30)

   # -- Menu -- # 
   Menu = ["Press 'a' to play Sound Effect #1", "Press 's' to play Sound Effect #2", "Press 'b' to play background music", "Press 'p' to pause the background music", "Press 'f' to unpause the background music", "Press 'r' to generate a random text color", "Press 'u' to change the background"]

   # -- Offset -- # 
   base_y = 30 # starting y-value for the top of menu
   line_height = 60 # Number of pixels between each text


   # -- Load and Set Up Graphic -- #
   background_image = pygame.image.load("C:\Project-Text-Menu\halloween-scary-ghost-face-illustration-cartoon-hd-png-701751694865357gijwaaz3fi-removebg-preview.png").convert()
   background_image.set_colorkey(BLACK)

   running = True
   while running:
      running = handle_events()

      screen.fill(WHITE) # Use color from config

      # -- If Key Pressed -- # 
      keys = pygame.key.get_pressed()
      if keys[pygame.K_a]:
         roblox_soundL.play()
      if keys[pygame.K_s]:
         lazer_soundL.play()
      if keys[pygame.K_b]:
         pygame.mixer.music.play()
      if keys[pygame.K_p]:
         pygame.mixer.music.pause()
      if keys[pygame.K_f]:
         pygame.mixer.music.unpause()
      if keys[pygame.K_r]:
         random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
         text_color = random_color
      else: 
         text_color = GREEN
      if keys[pygame.K_u]:
         screen.blit(background_image, [200,200])
      

      # -- Move Through Menu -- #
      for i in range(len(Menu)): 
         draw_text(screen, Menu[i], text_font, text_color, base_y + i * line_height)


      # -- Loop Through For loop -- # 
      for event in pygame.event.get(): 
         if event.type == pygame.QUIT: 
            running = False


      pygame.display.flip()

      # -- Limit the frame rate to the specified frames per second (FPS) -- #
      clock.tick(FPS) # Use the clock to control the frame rate

   pygame.quit()
   sys.exit()

if __name__ == "__main__":
   main()