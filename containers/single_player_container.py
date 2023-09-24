import pygame
import pygame_gui
from pygame.surface import Surface
from pygame.event import Event


from game import Game, GameFieldRenderer
from game.point import Point
from containers import Container, GameSounds
from constants import WINDOWWIDTH, WINDOWHEIGHT, BACKGROUNDPATH
from gui.single_player_ui import SinglePlayerMenu

class SinglePlayerContainer(Container, GameSounds):
    def __init__(self, window_surface):
        super().__init__(window_surface)
        GameSounds.__init__(self)

        self.renderer = GameFieldRenderer()
        self.game = Game()


        self.sp_surface = Surface((WINDOWWIDTH, WINDOWHEIGHT))
        self.sp_surface.blit(pygame.image.load(BACKGROUNDPATH), (0, 0))
        self.gamefield_pos_x =  40
        self.gamefield_pos_y = 100

        #interface objects
        self.manager = pygame_gui.UIManager((WINDOWWIDTH, WINDOWHEIGHT))


        self.sp_ui_menu = SinglePlayerMenu(self.manager, self.game, self.sp_surface)

        self.freeze_sound = pygame.mixer.Sound('resources/sfx-1.mp3')
        self.freeze_sound.set_volume(0.5)

        self.burn_sound = pygame.mixer.Sound('resources/sfx-2.mp3')
        self.burn_sound.set_volume(0.5)

        self.game_over = pygame.mixer.Sound('resources/game-over.mp3')
        self.game_over.set_volume(0.1)

        self.music = pygame.mixer.Sound('resources/8_bit_-_Korobejniki.mp3')
        self.music.set_volume(0.5)
        self.music.play(-1)

    @property
    def status(self):
        if self.game.is_game_over:
            self.music.stop()
            self.game_over.play()
            return 'menu'
        return None

    def event_handler(self, event: Event):
        self.manager.process_events(event)
        if not self.sp_ui_menu.pause_state:

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.game.key_left_down()
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.game.key_right_down()
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.game.key_up_down()
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.game.key_down_down()
                if event.key == pygame.K_SPACE:
                    self.game.key_space_down()

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.game.key_down_up()
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.game.key_left_up()
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.game.key_right_up()

        self.sp_ui_menu.event_handler(event)

    def update(self, time_delta: float):
        if not self.sp_ui_menu.pause_state:
            self.game.update(time_delta)
            self.manager.update(time_delta)
            self.sp_ui_menu.update()

            if self.game.is_field_updated:
                self.sfx_play()
        else:
            self.manager.update(time_delta)

    def render(self):
        game_data = self.game.dump()
        game_field_surface = self.renderer.render(game_data)
        self.sp_surface.blit(game_field_surface, (self.gamefield_pos_x, self.gamefield_pos_y))
        #game field frame (is it better to incorporate in renderer?)
        self.sp_surface.blit(pygame.image.load("resources/game_field_frame.png"), (self.gamefield_pos_x - 18, self.gamefield_pos_y - 15))

        self.manager.draw_ui(self.sp_surface)

        self.window_surface.blit(self.sp_surface, (0, 0))

    def sfx_play(self):
        if self.game.burned_rows == 4:
            self.burn_tetris.play()
        elif self.game.burned_rows:
            self.burn_sound.play()
        else:
            self.freeze_sound.play()
