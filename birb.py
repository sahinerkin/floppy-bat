import pygame

GRAVITY = -1
MAX_VELOCITY = 25

class Birb():
    def __init__(self, pos_x, pos_y):
        self._x = pos_x
        self._y = pos_y
        self._velocity = 0
        self.load_sprites()
        self.current_sprite = 0
        self.sprite_tick = -1
        self.sprite_refresh = 6

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


    def jump(self):
        self.velocity = 15
        self.sprite_tick = 0
        self.current_sprite = 0

    def tick(self):
        self.velocity += GRAVITY
        self._y -= self.velocity

        if self.sprite_tick > -1:
            self.sprite_tick += 1

        if self.sprite_tick >= self.sprite_refresh:
            self.sprite_tick = 0
            self.current_sprite += 1

        if self.current_sprite > 4:
            self.current_sprite = 0
            self.sprite_tick = -1

    def draw(self, screen):
        sprite = self.sprites[self.current_sprite]
        sprite_rect = sprite.get_rect(center=(self.x-15, self.y))
        screen.blit(sprite, sprite_rect)
        # pygame.draw.circle(screen, (255, 255, 0), (self.x, self.y), 15)

    def load_sprites(self):
        self.sprites = []

        for i in range(5):
            img_original = pygame.image.load(f"./assets/bat/frames/bat_32x32_f_{i}.png")
            self.sprites.append(pygame.transform.flip(pygame.transform.scale(img_original, (72, 72)), flip_x=True, flip_y=False))


def sign(num):
    return 1 if num >= 0 else -1