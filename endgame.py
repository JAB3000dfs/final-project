import pygame

pygame.init()

# Sets the window screen to
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
screen = pygame.display.set_mode((1000, 600))
screen.fill(red)

# Initial Page Setup
# Font
title_font = pygame.font.Font('avgr45w (3).ttf', 100)
text_font = pygame.font.Font('avgr45w (3).ttf', 40)
text_font.set_bold(True)
title_font.set_bold(True)
# Title
game_over = title_font.render("TITLE", True, black)

game_over_rectangle = game_over.get_rect()
game_over_rectangle.center = (500, 200)

screen.blit(game_over, game_over_rectangle)

while True:
    pygame.display.update()
