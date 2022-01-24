import random

from pipe import Pipe, PipeType
from constants import SCREEN_SIZE, CLOCK_FREQUENCY
from score_collider import ScoreCollider


# TRY KEEPING THE ACCELERATE AMOUNT VERY LOW (~0.5%) COMPARED TO STARTING VELOCITY
# OR ELSE PIPES MAY OVERLAP
# IF IT DOESN'T OVERLAP THE FIRST TIME (FIRST VELOCITY INCREASE), IT WON'T OVERLAP LATER


class PipeSpawner():

    _instance = None

    current_scroll_vel = 0
    def __init__(self, spawn_interval_ms, starting_velocity, accelerate_interval_ms, accelerate_amount):

        PipeSpawner._instance = self

        self._spawn_interval_ms = spawn_interval_ms
        self._spawn_timer_limit = spawn_interval_ms/1000 * CLOCK_FREQUENCY

        self._accelerate_interval_ms = accelerate_interval_ms
        self._accelerate_amount = accelerate_amount
        self._accelerate_timer_limit = accelerate_interval_ms/1000 * CLOCK_FREQUENCY

        self._starting_velocity = starting_velocity


    def reset(self):
        self._spawn_timer_count = self._spawn_timer_limit
        self._accelerate_timer_count = 0
        self._pipes = []
        self._score_colliders = []
        PipeSpawner.current_scroll_vel = self._starting_velocity

    @staticmethod
    def getInstance() -> "PipeSpawner":
        return PipeSpawner._instance

    def tick(self):
        self._spawn_timer_count += 1
        self._accelerate_timer_count += 1

        for pipe in self._pipes:
            if pipe._x < -200:
                self._pipes.remove(pipe)
            pipe.tick()

        for sc in self._score_colliders:
            if sc._left < -200:
                self._score_colliders.remove(sc)
            sc.tick()

        if self._accelerate_timer_count >= self._accelerate_timer_limit:
            self._accelerate_timer_count = 0
            PipeSpawner.current_scroll_vel += self._accelerate_amount
        
        if self._spawn_timer_count >= self._spawn_timer_limit:
            self._spawn_timer_count = 0
            pipes_midpoint = random.randint(200, 500)
            pipes_space = random.randint(260, 300)

            self._pipes.append(
                Pipe(pos_x=SCREEN_SIZE[0]+100,
                length=(pipes_midpoint-pipes_space//2),
                velocity=PipeSpawner.current_scroll_vel,
                type=PipeType.TOP_PIPE))

            self._pipes.append(
                Pipe(pos_x=SCREEN_SIZE[0]+100,
                length=SCREEN_SIZE[1]-(pipes_midpoint+pipes_space//2),
                velocity=PipeSpawner.current_scroll_vel,
                type=PipeType.BOTTOM_PIPE))

            self._score_colliders.append(
                ScoreCollider(left=SCREEN_SIZE[0]+100,
                              top=pipes_midpoint-pipes_space//2,
                              width=40,
                              height=pipes_space,
                              velocity=PipeSpawner.current_scroll_vel))
    
    def draw_pipes(self, screen):
        for pipe in self._pipes:
            pipe.draw(screen)