import sys
import pygame

WINDOWWIDTH = 600
WINDOWHEIGHT = 600


if __name__ == '__main__':
    pygame.init()
    windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
