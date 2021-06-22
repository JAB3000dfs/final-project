import pygame

pygame.init()
def endgame(points, function):
    # Sets the window screen to
    white = (255, 255, 255)
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

    score = score_font.render("points:" + str(points), True, black)
    score_rectangle = score.get_rect()
    game_over_rectangle = game_over.get_rect()
    game_over_rectangle.center = (500, 200)
    score_rectangle.center = (500, 400)
    play_again_rectangle = play_again.get_rect()
    play_again_rectangle.center = (500, 500)

    screen.blit(game_over, game_over_rectangle)
    screen.blit(score, score_rectangle)
    screen.blit(play_again, play_again_rectangle)

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
                    function

        pygame.display.update()
