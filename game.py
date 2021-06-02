# Imports
import pygame
import random

# Hitponts function
# Hitpoints decrease by 5 every second touched by troop or bullet
white = (255, 255, 255)
colour = (69, 5, 189)
black = (0, 0, 0)


def place_troops(screen):
    p = 500
    q = 500
    for i in range(47):

        # Loads the Spongebob sprite
        spongebob = pygame.image.load("spongebob.png")

        # Resizes the sprite to be 200x187
        spongebob = pygame.transform.scale(spongebob, (60, 54))
        spongebob_position = [p, q]
        q -= 10
        # Sets the sprite position

        screen.blit(spongebob, spongebob_position)
        pygame.display.update()

def start_game():
    spongebob = pygame.image.load("spongebob.png")
    spongebob = pygame.transform.scale(spongebob, (60, 54))
    p = 500
    q = 500
    spongebob_position = [p, q]
    mouse_x = 500
    screen = pygame.display.set_mode((1000, 600))
    screen.fill(white)
    start_game = True
    pygame.draw.polygon(screen, colour, ((250, 600), (750, 600), (750, 531), (250, 531)))
    pygame.draw.line(screen, black, (495, 531), (495, 500), 10)
    pygame.draw.polygon(screen, colour, ((250, 0), (750, 0), (750, 69), (250, 69)))
    pygame.draw.line(screen, black, (495, 69), (495, 100), 10)
    while True:
        y = 100
        a = random.randint(250, 751)
        b = 500
        while start_game == True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEMOTION:
                    # Gets the coordinates of the mouse
                    mouse_x = pygame.mouse.get_pos()[0]

            # Create ally building


            pygame.draw.circle(screen, black, (mouse_x, b), 10)
            b = b - 1

            # Assign building number of hitpoints
            # When hitpoints go to 0 building disappears you won screen appears

            # Create enemy building)s

            pygame.draw.circle(screen, black, (a, y), 10)
            y = y + 1

            for event in pygame.event.get():
                # Checks for keys that have been pressed
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        q -= 10
                        screen.blit(spongebob, spongebob_position)
                        check = True
            pygame.draw.circle(screen, white, (a, y), 10)
            y = y + 1
            pygame.draw.circle(screen, white, (mouse_x, b), 10)
            b = b - 1



            if (y == 300):
                break

            pygame.display.update()

    # Assign building number of hitpoints
    # When hitpoints go to 0 building disappears, game over screen appears

# Troop Class containing all info about troops
# Assign Number of Hitpoints
# Speed of troop

# Direpygame.display.quit()


# tower defense class
# speed of bullets
# rate of fire

# Keyboard interactions
# Spawn troops
# Esc to quit and go to initial page

# Mouse interactions
# Shoot tower defense in direction of mouse
# Move mouse sprite
# When clicked start clicked, start game
# When info button clicked, go to info page for user on how to play and features of the game

# Game Over function
# If user won show winning page
# If user lost show losing page