import pygame
import random
import time

def start_game2():
    white = (255, 255, 255)
    colour = (69, 5, 189)
    black = (0, 0, 0)
    screen = pygame.display.set_mode((1000, 600))
    screen.fill(white)


    t_end = time.time() + 4
    pygame.draw.circle(screen, black, (random.randint(250, 751), random.randint(250, 751)), 10)
    pygame.display.update()
    while time.time() < t_end:
        pass
    screen.fill(white)

start_game2()
