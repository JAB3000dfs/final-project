import pygame
import random
import time

def start_game2():
    while True:
        white = (255, 255, 255)
        colour = (69, 5, 189)
        black = (0, 0, 0)
        screen = pygame.display.set_mode((1000, 600))
        screen.fill(white)

        t_end = time.time() + 4
        x = random.randint(250, 350)
        y = random.randint(250, 350)
        pygame.draw.circle(screen, black, (x, y), 20)
        pygame.display.update()
        while time.time() < t_end:
            pass

