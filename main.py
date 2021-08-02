# Imports and initialising Pygame

import pygame
from sys import exit
from functions import start_game
from functions import start_screen

# Initialise Pygame
pygame.init()

# Colour variables
black = (0, 0, 0)
pastel_blue = (186, 230, 255)

# Sets the window screen to 1000 x 600 and fills it in
screen = pygame.display.set_mode((1000, 600))

# Font
text_font = pygame.font.Font('avgr45w (3).ttf', 40)
text_font.set_bold(True)
instructions_font = pygame.font.Font('avgr45w (3).ttf', 20)

# Displays start screen
start_screen()

# Initialize mouse variables
mouse_x = 12000
mouse_y = 12000

while True:

    for event in pygame.event.get():
        # Getting the mouse x and y values
        if event.type == pygame.MOUSEMOTION:
            mouse_x = pygame.mouse.get_pos()[0]
            mouse_y = pygame.mouse.get_pos()[1]

        # Allows user to close the game when clicking the x button
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the start button is clicked, start game
            if 380 < mouse_x < 620 and 395 < mouse_y < 405:
                start_game()

            # If the instructions button is clicked, display instructions
            elif 370 < mouse_x < 630 and 480 < mouse_y < 520:
                screen.fill(pastel_blue)

                # Displays instructions
                instructions_line_1 = "Click on the targets as fast as you can"
                instructions = instructions_font.render(instructions_line_1, True, black)
                instructions_rectangle = instructions.get_rect()
                instructions_rectangle.center = (500, 100)
                screen.blit(instructions, instructions_rectangle)

                instructions_line_2 = "Click on the targets as fast as you can"
                instructions2 = instructions_font.render(instructions_line_2, True, black)
                instructions2_rectangle = instructions2.get_rect()
                instructions2_rectangle.center = (500, 150)
                screen.blit(instructions2, instructions2_rectangle)

                instructions_line_3 = "If you don't click on the targets fast enough you lose a life"
                instructions3 = instructions_font.render(instructions_line_3, True, black)
                instructions3_rectangle = instructions3.get_rect()
                instructions3_rectangle.center = (500, 200)
                screen.blit(instructions3, instructions3_rectangle)

                instructions_line_4 = "3 deaths and you're out"
                instructions4 = instructions_font.render(instructions_line_4, True, black)
                instructions4_rectangle = instructions4.get_rect()
                instructions4_rectangle.center = (500, 250)
                screen.blit(instructions4, instructions4_rectangle)

                back_home = text_font.render(" <--", True, black)
                back_home_rectangle = back_home.get_rect()
                back_home_rectangle.center = (100, 100)
                screen.blit(back_home, back_home_rectangle)

            # If the back arrow is clicked, go to start screen
            if 50 < mouse_x < 150 and 0 < mouse_y < 600:
                start_screen()

        # Updates the screen
        pygame.display.update()
