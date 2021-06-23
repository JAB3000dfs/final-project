# Imports
import pygame
import random
import time

# Colour variables
white = (255, 255, 255)
black = (0, 0, 0)
lavender = (193, 186, 255)
red = (255, 0, 0)

# Sets the window screen to 1000 x 600 and fills it in
screen = pygame.display.set_mode((1000, 600))
screen.fill(lavender)

# Font Info
title_font = pygame.font.Font('Questrial-Regular.ttf', 80)
text_font = pygame.font.Font('avgr45w (3).ttf', 40)
text_font.set_bold(True)
title_font.set_bold(True)

# Title
title = title_font.render("TARGET PRACTICE", True, black)
title_rectangle = title.get_rect()
title_rectangle.center = (500, 200)

# Start button
start_button = text_font.render("START", True, black)
start_rectangle = start_button.get_rect()
start_rectangle.center = (500, 400)

# Instructions button
instructions_button = text_font.render("Instructions", True, black)
instructions_button_rectangle = instructions_button.get_rect()
instructions_button_rectangle.center = (500, 500)

# Function that sets up initial screen
def start_screen():
    screen.fill(lavender)
    screen.blit(instructions_button, instructions_button_rectangle)
    screen.blit(start_button, start_rectangle)
    screen.blit(title, title_rectangle)

def endgame(points):
    # Sets the window screen
    black = (0, 0, 0)
    red = (255, 0, 0)
    screen = pygame.display.set_mode((1000, 600))
    screen.fill(red)
    # Initial Page Setup
    # Font
    title_font = pygame.font.Font('avgr45w (3).ttf', 100)
    title_font.set_bold(True)
    text_font = pygame.font.Font('avgr45w (3).ttf', 40)
    text_font.set_bold(True)
    score_font = pygame.font.Font('avgr45w (3).ttf', 40)

    # Title
    game_over = title_font.render("YOU SUCK", True, black)

    # Create start button sprit
    play_again = text_font.render("Play again", True, black)
    instructions = text_font.render("Instructions", True, black)

    score = score_font.render("points:" + str(points), True, black)
    score_rectangle = score.get_rect()
    game_over_rectangle = game_over.get_rect()
    game_over_rectangle.center = (500, 200)
    score_rectangle.center = (500, 300)
    play_again_rectangle = play_again.get_rect()
    play_again_rectangle.center = (500, 400)
    instructions_rectangle = instructions.get_rect()
    instructions_rectangle.center = (500, 500)

    screen.blit(game_over, game_over_rectangle)
    screen.blit(score, score_rectangle)
    screen.blit(play_again, play_again_rectangle)
    screen.blit(instructions, instructions_rectangle)

    pygame.display.update()

def start_game():

    # Initial variables
    points = 0          # number of points
    strikes = 3         # number of strikes left
    mouse_x = 0         # mouse_x position
    mouse_y = 0         # mouse_y position
    speed = 4           # how long ball stays on the screen

    # Fill screen
    screen.fill(white)

    # Initial x and y values for the ball (doesn't show up on the screen)
    x = 12000
    y = 12000


    while True:
        for event in pygame.event.get():
            # Getting the mouse x and y values
            if event.type == pygame.MOUSEMOTION:
                mouse_x = pygame.mouse.get_pos()[0]
                mouse_y = pygame.mouse.get_pos()[1]

        # Timer loop
        t_end = time.time() + speed

        # If the mouse is in the same place as the ball, increase points
        if x + 40 >= mouse_x >= x - 40 and y + 40 >= mouse_y >= y - 40:
            points += 1000
            print(points)

        # If not, decrease number of strikes left
        else:
            strikes -= 1

            # If strikes left < 0, show endgame screen
            if strikes < 0:
                endgame(points)
                break

        # each time the player hits three targets they have 25% less time to click on the next targets
        if points % 3 == 0:
            speed /= 1.25

        # spawns circle in a random location
        x = random.randint(20, 980)
        y = random.randint(20, 580)

        three = random.randint(0, 255)
        two = random.randint(0, 255)
        one = random.randint(0, 255)
        colour = (three, two, one)

        screen.fill(colour)
        pygame.draw.circle(screen, black, (x, y), 40)

        # displays the amount of points the player has
        score_font = pygame.font.Font('avgr45w (3).ttf', 20)
        score = score_font.render("Score: " + str(points), True, black)
        score_rectangle = score.get_rect()
        score_rectangle.center = (75, 25)
        screen.blit(score, score_rectangle)

        #displays the amount of lives the player has
        lives_font = pygame.font.Font('avgr45w (3).ttf', 20)
        lives = lives_font.render("Lives: " + str(strikes + 1), True, black)
        lives_rectangle = lives.get_rect()
        lives_rectangle.center = (925, 25)

        screen.blit(lives, lives_rectangle)

        # updates the screen
        pygame.display.update()

        # allows the player time to position their mouse on the target
        while time.time() < t_end:
            pass
