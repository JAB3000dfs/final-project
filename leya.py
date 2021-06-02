import pygame

def place_troops(screen):
    for i in range(10):
        p = 500
        q = 500
        # Loads the Spongebob sprite
        spongebob = pygame.image.load("spongebob.png")

        # Resizes the sprite to be 200x187
        spongebob = pygame.transform.scale(spongebob, (60, 54))
        spongebob_position = [p, q]
        q += 10
        # Sets the sprite position

        screen.blit(spongebob, spongebob_position)
        pygame.display.update()