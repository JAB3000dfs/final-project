import pygame

pygame.init()

# Sets the window screen to
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
screen = pygame.display.set_mode((1000, 600))
screen.fill(red)
points = 17
# Initial Page Setup
# Font
title_font = pygame.font.Font('avgr45w (3).ttf', 100)
title_font.set_bold(True)
score_font = pygame.font.Font('avgr45w (3).ttf', 40)
# Title
game_over = title_font.render("YOU SUCK", True, black)

score = score_font.render(str(points), True, black)
score_rectangle = score.get_rect()
game_over_rectangle = game_over.get_rect()
game_over_rectangle.center = (500, 200)
score_rectangle.center = (500, 400)
screen.blit(game_over, game_over_rectangle)
screen.blit(score, score_rectangle)

while True:
    pygame.display.update()
