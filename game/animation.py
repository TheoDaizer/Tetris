import pygame
from enum import IntEnum
from constants import TILESIZE

BURN_ANIMATION_SIZE = (4, 4)


class AnimationType(IntEnum):
    BURN_ANIMATION = 0
    SIZE = 1


class Animation:

    burn_animation = pygame.image.load("resources/explosion_pixelfied.png")

    burn_frames = []
    for i in range(16):
        r = pygame.Rect(i % BURN_ANIMATION_SIZE[0] * TILESIZE, i // BURN_ANIMATION_SIZE[1] * TILESIZE, TILESIZE, TILESIZE)
        burn_frames.append(burn_animation.subsurface(r))

    frames_container = (burn_frames, )

    def __init__(self, animation_type: AnimationType, num_of_frames: int, update_time: int = 30):
        self.animation_type = animation_type

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
