from enum import Enum
from bat import Bat
import pygame

pipe_body_original = pygame.image.load("./assets/pipes/pipe_body.png")
pipe_exit_original = pygame.image.load("./assets/pipes/pipe_exit.png")

class PipeType(Enum):
    TOP_PIPE = 0
    BOTTOM_PIPE = 1

class Pipe():
    def __init__(self, pos_x, length, velocity, type=PipeType.BOTTOM_PIPE):
        self.pos_x = pos_x
        self.length = length
        self.velocity = velocity
        self.type = type

        self.pipe_body_sprite = pygame.transform.scale(pipe_body_original, (80, self.length))
        self.pipe_exit_sprite = pygame.transform.scale(pipe_exit_original, (80, 35))

        if self.type == PipeType.TOP_PIPE:
            self.pipe_body_sprite = pygame.transform.flip(self.pipe_body_sprite, flip_x=False, flip_y=True)
            self.pipe_exit_sprite = pygame.transform.flip(self.pipe_exit_sprite, flip_x=False, flip_y=True)

    
    def draw(self, screen:pygame.Surface):
        

        if self.type == PipeType.TOP_PIPE:
            self.pipe_body_rect = self.pipe_body_sprite.get_rect(midtop=(self.pos_x, 0))
            self.pipe_exit_rect = self.pipe_exit_sprite.get_rect(midtop=(self.pos_x, self.length))   
        else:
            self.pipe_body_rect = self.pipe_body_sprite.get_rect(midbottom=(self.pos_x, screen.get_height()))
            self.pipe_exit_rect = self.pipe_exit_sprite.get_rect(midbottom=(self.pos_x, screen.get_height()-self.length))
        
        screen.blit(self.pipe_body_sprite, self.pipe_body_rect)
        screen.blit(self.pipe_exit_sprite, self.pipe_exit_rect)

    def tick(self):
        self.pos_x -= self.velocity
        if self.pipe_body_rect.colliderect(Bat.getInstance().sprite_rect):
            print("Collision!")
            pass
    