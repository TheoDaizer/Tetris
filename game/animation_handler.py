import pygame
from constants import TILESIZE


class Animation:

    def __init__(self, num_of_frames: int = 16, update_time: int = 30):
        self.frame = 0
        self.num_of_frames = num_of_frames
        self.time = 0
        self.update_time = update_time

    def update(self, dt):
        self.time += dt
        while self.time > self.update_time:
            self.frame += 1
            self.time -= self.update_time
            if self.frame >= self.num_of_frames:
                return False
        return True


# if __name__ == '__main__':
#     pygame.init()
#     display_width = 800
#     display_height = 600
#     gameDisplay = pygame.display.set_mode((display_width, display_height))
#
#     clock = pygame.time.Clock()
#
#     animation = Animation()
#
#     while True:
#         dt = clock.tick(60)
#
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#
#         animation.update(dt)
#
#         gameDisplay.fill("black")
#
#         #r = pygame.Rect(0, 0, TILESIZE, TILESIZE)
#         #gameDisplay.blit(animation.frames[animation.frame], r)
#
#         # for i in range(animation.num_of_frames):
#         #    r = pygame.Rect(i // 4 * TILESIZE, i % 4 * TILESIZE, TILESIZE, TILESIZE)
#         #    gameDisplay.blit(animation.frames[i], r)
#
#         pygame.display.update()

