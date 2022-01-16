import pygame

GRAVITY = -1
MAX_VELOCITY = 25

class Birb():
    def __init__(self, pos_x, pos_y):
        self._x = pos_x
        self._y = pos_y
        self._velocity = 0

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

    def tick(self):
        self.velocity += GRAVITY
        self._y -= self.velocity

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 0), (self.x, self.y), 15)


def sign(num):
    return 1 if num >= 0 else -1