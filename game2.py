import pygame
import random
import time

def start_game2():
    points = 0
    strikes = 3
    mouse_x = 0
    mouse_y = 0
    white = (255, 255, 255)
    screen = pygame.display.set_mode((1000, 600))
    screen.fill(white)
    x = 0
    y = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                mouse_x = pygame.mouse.get_pos()[0]
                mouse_y = pygame.mouse.get_pos()[1]
        black = (0, 0, 0)
        t_end = time.time() + 4
        if x + 20 >= mouse_x >= x - 20 and y + 20 >= mouse_y >= y - 20:
            points += 1
            print(points)
        else:
            strikes -= 1
            if (strikes < 0):
                screen.fill(black)
                break
        x = random.randint(20, 980)
        y = random.randint(20, 580)
        screen.fill(white)
        pygame.draw.circle(screen, black, (x, y), 20)
        pygame.display.update()
        while time.time() < t_end:
            pass

