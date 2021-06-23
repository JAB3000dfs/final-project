# Imports
import pygame
from functions import start_game
from functions import start_screen

pygame.init()

# game function
def game():

    # Colour variables
    white = (255, 255, 255)
    black = (0, 0, 0)
    pastel_blue = (186, 230, 255)

    # Sets the window screen to 1000 x 600 and fills it in
    screen = pygame.display.set_mode((1000, 600))
    screen.fill(white)

    # Font
    text_font = pygame.font.Font('avgr45w (3).ttf', 40)
    text_font.set_bold(True)
    instructions_font = pygame.font.Font('avgr45w (3).ttf', 20)

    # Displays start screen
    start_screen()

    while True:
        # Checks for mouse activity
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                #                 # Gets the coordinates of the mouse
                mouse_x = pygame.mouse.get_pos()[0]
                mouse_y = pygame.mouse.get_pos()[1]
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the start button is clicked, start game
                if (380 < mouse_x < 620 and 395 < mouse_y < 405):
                    start_game()

                # If the instructions button is clicked, display instructions
                elif (370 < mouse_x < 630 and 480 < mouse_y < 520):
                    screen.fill(pastel_blue)
                    instructions = instructions_font.render("Click on the targets as fast as you can", True, black)
                    instructions_rectangle = instructions.get_rect()
                    instructions_rectangle.center = (500, 100)
                    screen.blit(instructions, instructions_rectangle)

                    instructions2 = instructions_font.render("You have less and less time as the game progress's", True, black)
                    instructions2_rectangle = instructions2.get_rect()
                    instructions2_rectangle.center = (500, 150)
                    screen.blit(instructions2, instructions2_rectangle)

                    instructions3 = instructions_font.render("If you don't click on the targets fast enough you lose a life", True, black)
                    instructions3_rectangle = instructions3.get_rect()
                    instructions3_rectangle.center = (500, 200)
                    screen.blit(instructions3, instructions3_rectangle)

                    instructions4 = instructions_font.render("3 deaths and you're out", True, black)
                    instructions4_rectangle = instructions4.get_rect()
                    instructions4_rectangle.center = (500, 250)
                    screen.blit(instructions4, instructions4_rectangle)

                    back_home = text_font.render(" <--", True, black)
                    back_home_rectangle = back_home.get_rect()
                    back_home_rectangle.center = (100, 100)
                    screen.blit(back_home, back_home_rectangle)

                # If the back arrow is clicked, go to start screen
                if (50 < mouse_x < 150 and 0 < mouse_y < 600):
                    start_screen()

        pygame.display.update()

# Run the whole game function
game()

