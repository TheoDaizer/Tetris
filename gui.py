import sys

import pygame
import pygame_gui

from constants import *
from render import render
import game

if __name__ == '__main__':

    pygame.init()
    pygame.display.set_caption('PvP Tetris')
    clock = pygame.time.Clock()

    window_surface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), pygame.RESIZABLE)
    background = pygame.Surface((WINDOWWIDTH, WINDOWHEIGHT))
    background.fill(pygame.Color('#000000'))
    manager = pygame_gui.UIManager((WINDOWWIDTH, WINDOWHEIGHT))

    confirm_start_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((10, 240), (300, 100)),
                                                        text='Press Space to Start',
                                                        manager=manager,
                                                        visible=False
                                                        )

    def starting_screen():

        while True:

            confirm_start_button.visible = True

            dt_frame = clock.tick(FPS)  # time from previous frame in milliseconds. argument provides fps limitation
            dt_input = dt_frame / 1000.0  # time from previous input recognition in milliseconds, divisor for refresh rate

            # input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        single_plyer()

                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == confirm_start_button:
                        single_plyer()

                manager.process_events(event)

            manager.update(dt_input)

            window_surface.blit(background, (0, 0))
            manager.draw_ui(window_surface)

            pygame.display.update()

    def single_plyer():

        tetris_game = game.Game()
        running = True
        clock.tick()  # time restart
        while running:
            dt_frame = clock.tick(FPS)  # time from previous frame in milliseconds. argument provides fps limitation

            # input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            tetris_game.update(dt_frame)

            window_surface.fill("black")  # "clearing screen" by filling it with one color
            render(tetris_game, window_surface)
            pygame.display.flip()  # updating screen

    starting_screen()
