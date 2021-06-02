# Imports
import pygame
from Betterperson import start_game
from Betterperson import place_troops

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

while True:
    # Checks for mouse activity
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            # Gets the coordinates of the mouse
            mouse_x = pygame.mouse.get_pos()[0]
            mouse_y = pygame.mouse.get_pos()[1]
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Checks whether the start button is clicked
            if (420 < mouse_x < 580 and 395 < mouse_y < 405):

                start_game()
                while (start_game == True):
                    for event in pygame.event.get():
                        # Checks for keys that have been pressed
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                place_troops(screen)


            # Checks whether the instructions button is clicked
            elif (370 < mouse_x < 630 and 480 < mouse_y < 520):
                screen.fill(white)
                instructions = text_font.render("stuff", True, black)
                instructions_rectangle = instructions.get_rect()
                instructions_rectangle.center = (500, 100)
                screen.blit(instructions, instructions_rectangle)

                back_home = text_font.render(" <--", True, black)
                back_home_rectangle = back_home.get_rect()
                back_home_rectangle.center = (100, 100)
                screen.blit(back_home, back_home_rectangle)

            if (50 < mouse_x < 150 and 0 < mouse_y < 600):
                start_screen()

    pygame.display.update()
