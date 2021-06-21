import pygame
import random
import time

def start_game2():
    points = 0
    mouse_x = 0
    mouse_y = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                mouse_x = pygame.mouse.get_pos()[0]
                mouse_y = pygame.mouse.get_pos()[1]
        white = (255, 255, 255)
        colour = (69, 5, 189)
        black = (0, 0, 0)
        screen = pygame.display.set_mode((1000, 600))
        screen.fill(white)

        t_end = time.time() + 4
        x = random.randint(250, 350)
        y = random.randint(250, 350)
        pygame.draw.circle(screen, black, (x, y), 20)
        if mouse_x >= x - 20 and mouse_x <= x + 20 and mouse_y >= x - 20 and mouse_y <= x + 20:
            points += 1
            print("points")
        pygame.display.update()
        while time.time() < t_end:
            pass

