import pygame
from numbers import Number
from constants import GRAVITY, CLOCK_FREQUENCY
MAX_VELOCITY = 4000

class Bat():
    _instance = None

    def __init__(self, pos_x, pos_y, jump_vel=900):
        self._x: Number = pos_x
        self._y: Number = pos_y
        self._jump_vel = jump_vel
        self._velocity = 0
        self.sprites_list = Bat.load_sprites()
        self.sprites_length = len(self.sprites_list)
        self.sprite_idx = 0
        self.sprite_tick = -1
        self._is_alive = True

        Bat._instance = self

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def velocity(self):
        return self._velocity

    @velocity.setter
    def velocity(self, new_vel):
        self._velocity = new_vel if abs(new_vel) < abs(MAX_VELOCITY) else MAX_VELOCITY * sign(new_vel)

    @staticmethod
    def getInstance() -> "Bat":
        return Bat._instance


    def jump(self, vel=None):
        if not self._is_alive:
            return

        self.velocity = self._jump_vel if vel is None else vel
        self.sprite_tick = 0
        self.sprite_idx = 0

    def tick(self):
        self.velocity += GRAVITY/CLOCK_FREQUENCY
        self._y -= self.velocity/CLOCK_FREQUENCY

        if not self._is_alive:
            return

        if self.sprite_tick > -1:
            self.sprite_tick += 1

        if self.sprite_tick >= self.sprites_length:
            self.sprite_tick = 0
            self.sprite_idx += 1

        if self.sprite_idx > 4:
            self.sprite_tick = -1
            self.sprite_idx = 0

        # print(self.sprite_rect.collidedict())


    def draw(self, screen:pygame.Surface):
        self.sprite = self.sprites_list[self.sprite_idx]
        self.sprite_rect = self.sprite.get_rect(center=(self.x, self.y))
        self.coll_rect = pygame.Rect(self.x, self.y-10, 25, 25)
        # pygame.draw.rect(screen, (255,0,0), rect=self.coll_rect)
        screen.blit(self.sprite, self.sprite_rect)
        # pygame.draw.circle(screen, (255, 255, 0), (self.x, self.y), 15)

    def load_sprites():
        sprites_list = []

        for i in range(6):
            img_original = pygame.image.load(f"./assets/bat/frames/bat_30x30_f_{i}.png").convert_alpha()
            sprites_list.append(pygame.transform.flip(pygame.transform.scale(img_original, (72, 72)), flip_x=True, flip_y=False))
        
        return sprites_list
    
    def die(self):
        self.jump(600)
        self._is_alive = False
        self.sprite_idx = 5


def sign(num):
    return 1 if num >= 0 else -1