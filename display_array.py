import pygame
from pygame.locals import *
from sys import exit


# Source: http://programarcadegames.com/index.php?lang=en&chapter=array_backed_grids
# You may need to install pygame

def display_array(arr, dim):
    # Define some colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (90, 90, 90)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    MAGENTA = (255, 102, 255)

    WIDTH = 20
    HEIGHT = 20
    MARGIN = 5

    pygame.init()

    # Set the width and height of the screen [width, height]
    WINDOW_SIZE = (500, 500)
    screen = pygame.display.set_mode(WINDOW_SIZE, RESIZABLE)

    pygame.display.set_caption("Array display")

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while not done:
        # Prevent "Not responding": allows pygame to handle internal actions
        pygame.event.pump()

        # Set screen background to black
        screen.fill(BLACK)

        for row in range(dim):
            for column in range(dim):
                color = WHITE
                if arr[row][column] == 'X':
                    color = GRAY
                elif arr[row][column] == 'S':
                    color = GREEN
                elif arr[row][column] == 'F':
                    color = RED
                elif arr[row][column] == "V":
                    color = MAGENTA
                pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * column + MARGIN,
                                                 (MARGIN + HEIGHT) * row + MARGIN,
                                                 WIDTH,
                                                 HEIGHT])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return pygame.quit()

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)


