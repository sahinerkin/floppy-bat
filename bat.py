import pygame

GRAVITY = -1
MAX_VELOCITY = 25


class Bat():
    _instance = None

    def __init__(self, pos_x, pos_y, jump_vel=15):
        self._x = pos_x
        self._y = pos_y
        self._jump_vel = jump_vel
        self._velocity = 0
        self.sprites_list = Bat.load_sprites()
        self.sprites_length = len(self.sprites_list)
        self.sprite_idx = 0
        self.sprite_tick = -1

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
    def getInstance():
        return Bat._instance


    def jump(self):
        self.velocity = self._jump_vel
        self.sprite_tick = 0
        self.sprite_idx = 0

    def tick(self):
        self.velocity += GRAVITY
        self._y -= self.velocity

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
        self.sprite_rect = self.sprite.get_rect(center=(self.x-15, self.y))
        screen.blit(self.sprite, self.sprite_rect)
        # pygame.draw.circle(screen, (255, 255, 0), (self.x, self.y), 15)

    def load_sprites():
        sprites_list = []

        for i in range(5):
            img_original = pygame.image.load(f"./assets/bat/frames/bat_32x32_f_{i}.png")
            sprites_list.append(pygame.transform.flip(pygame.transform.scale(img_original, (72, 72)), flip_x=True, flip_y=False))
        
        return sprites_list
    
    def die(self):
        self._jump_vel = 0


def sign(num):
    return 1 if num >= 0 else -1