import pygame
from numbers import Number
from constants import CLOCK_FREQUENCY, SCREEN_SIZE
from pipe_spawner import PipeSpawner

class Background():
    def __init__(self, layer_image_paths, layer_speed_multipliers):
        self.layers = []
        for i, path in enumerate(layer_image_paths):
            image_original = pygame.image.load(path).convert_alpha()
            layer = {
            "image": pygame.transform.scale(image_original, (image_original.get_width()/image_original.get_height()*SCREEN_SIZE[1], SCREEN_SIZE[1])),
            "speed_multiplier": layer_speed_multipliers[i],
            "pos_left": 0
            }

            layer["image_size"] = (layer["image"].get_width(), layer["image"].get_height())

            self.layers.append(layer)
    
    def tick(self):
        for layer in self.layers:
            layer["pos_left"] -= layer["speed_multiplier"]*PipeSpawner.current_scroll_vel/CLOCK_FREQUENCY
            if layer["pos_left"] < -layer["image_size"][0]:
                layer["pos_left"] = 0

    def draw(self, screen):
        for layer in self.layers:
            screen.blit(layer["image"], (layer["pos_left"], 0))
            screen.blit(layer["image"], (layer["pos_left"]+layer["image_size"][0], 0))
