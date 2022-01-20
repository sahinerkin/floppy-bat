from enum import Enum
from bat import Bat
import pygame

from constants import CLOCK_FREQUENCY

pipe_body_original = pygame.image.load("./assets/pipes/pipe_body.png")
pipe_exit_original = pygame.image.load("./assets/pipes/pipe_exit.png")


class PipeType(Enum):
    TOP_PIPE = 0
    BOTTOM_PIPE = 1

class Pipe():
    def __init__(self, pos_x, length, velocity, type=PipeType.BOTTOM_PIPE):
        self._x = pos_x
        self._length = length
        self._velocity = velocity
        self._type = type

        self.pipe_body_sprite = pygame.transform.scale(pipe_body_original.convert_alpha(), (80, self._length-35))
        self.pipe_exit_sprite = pygame.transform.scale(pipe_exit_original.convert_alpha(), (80, 35))

        if self._type == PipeType.TOP_PIPE:
            self.pipe_body_sprite = pygame.transform.flip(self.pipe_body_sprite, flip_x=False, flip_y=True)
            self.pipe_exit_sprite = pygame.transform.flip(self.pipe_exit_sprite, flip_x=False, flip_y=True)

    
    def draw(self, screen:pygame.Surface):
        if self._type == PipeType.TOP_PIPE:
            self.pipe_body_rect = self.pipe_body_sprite.get_rect(midtop=(self._x, 0))
            self.pipe_exit_rect = self.pipe_exit_sprite.get_rect(midtop=(self._x, self._length-35))   
        else:
            self.pipe_body_rect = self.pipe_body_sprite.get_rect(midbottom=(self._x, screen.get_height()))
            self.pipe_exit_rect = self.pipe_exit_sprite.get_rect(midbottom=(self._x, screen.get_height()-self._length+35))
        
        screen.blit(self.pipe_body_sprite, self.pipe_body_rect)
        screen.blit(self.pipe_exit_sprite, self.pipe_exit_rect)

    def tick(self):
        self._x -= self._velocity/CLOCK_FREQUENCY
        if self.pipe_body_rect.colliderect(Bat.getInstance().coll_rect) \
        or self.pipe_exit_rect.colliderect(Bat.getInstance().coll_rect):
            Bat.getInstance().die()
    