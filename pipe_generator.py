import random
from pipe import Pipe, PipeType
from constants import SCREEN_SIZE, CLOCK_FREQUENCY

class PipeGenerator():
    def __init__(self, time_interval_ms):
        self._time_interval_ms = time_interval_ms
        self._time_counter = 0
        self._counter_limit = time_interval_ms/1000 * CLOCK_FREQUENCY
        self._pipes = []

    def tick(self):
        self._time_counter += 1

        for pipe in self._pipes:
            pipe.tick()
        
        if self._time_counter >= self._counter_limit:
            self._time_counter = 0
            pipes_midpoint = random.randint(200, 500)
            pipes_space = random.randint(300, 340)

            self._pipes.append(
                Pipe(pos_x=SCREEN_SIZE[1]+100,
                length=(pipes_midpoint-pipes_space//2),
                velocity=120,
                type=PipeType.TOP_PIPE))

            self._pipes.append(
                Pipe(pos_x=SCREEN_SIZE[1]+100,
                length=SCREEN_SIZE[1]-(pipes_midpoint+pipes_space//2),
                velocity=120,
                type=PipeType.BOTTOM_PIPE))
    
    def draw_pipes(self, screen):
        for pipe in self._pipes:
            pipe.draw(screen)