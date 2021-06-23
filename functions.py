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
title_font.set_bold(True)
text_font = pygame.font.Font('avgr45w (3).ttf', 40)
text_font.set_bold(True)

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


# Function that creates game over screen
def game_over(points):
    # Fills the screen in red
    screen.fill(red)

    # Font
    game_over_title_font = pygame.font.Font('avgr45w (3).ttf', 100)
    game_over_title_font.set_bold(True)
    score_font = pygame.font.Font('avgr45w (3).ttf', 40)

    # Title
    game_over_title = title_font.render("YOU SUCK", True, black)
    game_over_rectangle = game_over_title.get_rect()
    game_over_rectangle.center = (500, 200)

    # Score
    score = score_font.render("points:" + str(points), True, black)
    score_rectangle = score.get_rect()
    score_rectangle.center = (500, 300)

    # Play again button
    play_again = text_font.render("Play again", True, black)
    play_again_rectangle = play_again.get_rect()
    play_again_rectangle.center = (500, 400)

    # Instructions button
    instructions = text_font.render("Instructions", True, black)
    instructions_rectangle = instructions.get_rect()
    instructions_rectangle.center = (500, 500)

    # Making everything appear
    screen.blit(game_over_title, game_over_rectangle)
    screen.blit(score, score_rectangle)
    screen.blit(play_again, play_again_rectangle)
    screen.blit(instructions, instructions_rectangle)

    # Updates the screen
    pygame.display.update()


# Start game function
def start_game():
    # Initial variables
    points = 0  # number of points
    strikes = 3  # number of strikes left
    mouse_x = 0  # mouse_x position
    mouse_y = 0  # mouse_y position
    speed = 4  # how long ball stays on the screen

    # Fill screen
    screen.fill(white)

    # Initial x and y values for the ball (doesn't show up on the screen)
    x = 12000
    y = 12000

    while True:
        # Getting the mouse x and y values
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                mouse_x = pygame.mouse.get_pos()[0]
                mouse_y = pygame.mouse.get_pos()[1]

        # If the mouse is in the same place as the ball, increase points
        if x + 40 >= mouse_x >= x - 40 and y + 40 >= mouse_y >= y - 40:
            points += 1000
            print(points)

        # If not, decrease number of strikes left
        else:
            strikes -= 1

            # If strikes left < 0, show game over screen
            if strikes < 0:
                game_over(points)
                break

        # Each time the player hits three targets they have 25% less time to click on the next targets
        if points % 3 == 0:
            speed /= 1.25

        # Makes the background a new random colour
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        colour = (r, g, b)
        screen.fill(colour)

        # Spawns circle in a random location
        x = random.randint(20, 980)
        y = random.randint(20, 580)
        pygame.draw.circle(screen, black, (x, y), 40)

        # Displays the amount of points the player has
        score_font = pygame.font.Font('avgr45w (3).ttf', 20)
        score = score_font.render("Score: " + str(points), True, black)
        score_rectangle = score.get_rect()
        score_rectangle.center = (75, 25)
        screen.blit(score, score_rectangle)

        # Displays the amount of lives the player has left
        lives_font = pygame.font.Font('avgr45w (3).ttf', 20)
        lives = lives_font.render("Lives: " + str(strikes + 1), True, black)
        lives_rectangle = lives.get_rect()
        lives_rectangle.center = (925, 25)
        screen.blit(lives, lives_rectangle)

        # Updates the screen
        pygame.display.update()

        # Gives the player time to position their mouse on the target
        t_end = time.time() + speed
        while time.time() < t_end:
            pass
