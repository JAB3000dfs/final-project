# Imports
import pygame
from game import start_game

pygame.init()

# Sets the window screen to
white = (255, 255, 255)
black = (0, 0, 0)
screen = pygame.display.set_mode((1000, 600))
screen.fill(white)

# Initial Page Setup
# Font
title_font = pygame.font.Font('avgr45w (3).ttf', 100)
text_font = pygame.font.Font('avgr45w (3).ttf', 40)
text_font.set_bold(True)
title_font.set_bold(True)
# Title
title = title_font.render("TITLE", True, black)

# Create start button sprit
start_button = text_font.render("START", True, black)

# Create Instructions Button
instructions_button = text_font.render("Instructions", True, black)

instructions_button_rectangle = instructions_button.get_rect()
instructions_button_rectangle.center = (500, 500)
start_rectangle = start_button.get_rect()
start_rectangle.center = (500, 400)
title_rectangle = title.get_rect()
title_rectangle.center = (500, 200)


# Initial screen function
def start_screen():
    screen.fill(white)
    screen.blit(instructions_button, instructions_button_rectangle)
    screen.blit(start_button, start_rectangle)
    screen.blit(title, title_rectangle)

start_screen()