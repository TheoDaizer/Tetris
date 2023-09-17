import pygame
import pygame_gui
from pygame.surface import Surface
from pygame.event import Event

from game import Game, GameFieldRenderer
from containers import Container, GameSounds
from constants import WINDOWWIDTH, WINDOWHEIGHT, BACKGROUNDPATH


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
        self.sp_ui_panel = pygame_gui.elements.ui_panel.UIPanel(
            relative_rect=pygame.Rect((400, 0), (200, 800)),
            manager=self.manager,
        )

        self.sp_ui_menu_panel = pygame_gui.elements.ui_panel.UIPanel(
            relative_rect=pygame.Rect((100, 200), (250, 400)),
            manager=self.manager,
            visible=False
        )

        # self.sp_next_figure_surface = pygame.Surface((100, 100))
        # self.sp_next_figure_item = self.renderer.render_figure(self.sp_next_figure_surface, self.game.figure.default_position, self.game.figure.next_shape, self.game.figure.default_orientation)

        #elements of game UI
        self.sp_next_figure_box = pygame_gui.elements.ui_image.UIImage (
            relative_rect=pygame.Rect((25, 25), (150, 100)),
            image_surface=pygame.image.load("resources/gtv_logo_mini.jpg"),
            container=self.sp_ui_panel,
            manager=self.manager,
            visible=True
        )

        self.sp_score_box = pygame_gui.elements.UITextBox(
            relative_rect=pygame.Rect((25, 125), (150, 100)),
            html_text="<p>Current Score: <br>" + str(self.game.score) + "</p>",
            container=self.sp_ui_panel,
            manager=self.manager,
            visible=True
        )

        self.sp_level_box = pygame_gui.elements.UITextBox(
            relative_rect=pygame.Rect((25, 225), (150, 100)),
            html_text="<p>Current Level: <br>" + str(self.game.level) + "</p>",
            container=self.sp_ui_panel,
            manager=self.manager,
            visible=True
        )

        self.sp_burned_total_box = pygame_gui.elements.UITextBox(
            relative_rect=pygame.Rect((25, 325), (150, 100)),
            html_text="<p>Rows burned: <br>" + str(self.game.burned_rows_total) + "</p>",
            container=self.sp_ui_panel,
            manager=self.manager,
            visible=True
        )

        #elements of ESC menu
        self.sp_btm_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((25, 275), (200, 100)),
            text='Back to Menu',
            container=self.sp_ui_menu_panel,
            manager=self.manager,
            visible=False
        )

        self.sp_mute_music_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((25, 75), (200, 100)),
            text='On/Off Music',
            container=self.sp_ui_menu_panel,
            manager=self.manager,
            visible=False
        )


        self.pause_state = False

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
        if not self.pause_state:

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

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if self.sp_ui_menu_panel.visible == False:
                    self.sp_ui_menu_panel.visible = True
                    self.sp_btm_button.visible = True
                    self.sp_mute_music_button.visible = True
                    self.pause_state = True
                    self.music.stop()
                else:
                    self.sp_ui_menu_panel.visible = False
                    self.sp_btm_button.visible = False
                    self.pause_state = False
                    self.sp_mute_music_button.visible = False
                    self.sp_surface.blit(pygame.image.load(BACKGROUNDPATH), (0, 0))
                    self.music.play(-1)

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.sp_btm_button:
                self.game.is_game_over = True
                self.music.stop()
                self.game_over.play()
                return 'menu'

            if event.ui_element == self.sp_mute_music_button:
                if self.music.get_volume() == 0.5:
                    self.freeze_sound.set_volume(0)
                    self.burn_sound.set_volume(0)
                    self.game_over.set_volume(0)
                    self.music.set_volume(0)
                else:
                    self.freeze_sound.set_volume(0.5)
                    self.burn_sound.set_volume(0.5)
                    self.game_over.set_volume(0.1)
                    self.music.set_volume(0.5)


    def update(self, time_delta: float):
        if not self.pause_state:
            self.game.update(time_delta)
            self.manager.update(time_delta)
            self.sp_score_box.set_text("<p>Current Score: <br>" + str(self.game.score) + "</p>")
            self.sp_level_box.set_text("<p>Current Level: <br>" + str(self.game.level) + "</p>")
            self.sp_burned_total_box.set_text("<p>Rows burned: <br>" + str(self.game.burned_rows_total) + "</p>")
            # if self.game.is_field_updated:
            #     self.sfx_play()
        else:
            self.manager.update(time_delta)

    def render(self):
        game_data = self.game.dump()
        game_field_surface = self.renderer.render(game_data)
        self.sp_surface.blit(game_field_surface, (self.gamefield_pos_x, self.gamefield_pos_y))
        self.manager.draw_ui(self.sp_surface)

        self.window_surface.blit(self.sp_surface, (0, 0))

    def sfx_play(self):
        if self.game.burned_rows == 4:
            self.burn_tetris.play()
        elif self.game.burned_rows:
            self.burn_sound.play()
        else:
            self.freeze_sound.play()
