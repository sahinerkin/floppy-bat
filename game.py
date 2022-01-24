from pygame import Surface
from background import *
from bat import *
from constants import *
from pipe_spawner import *

class Game():
    _instance = None

    def __init__(self):
        Game._instance = self
      
        self._font = pygame.font.Font('freesansbold.ttf', 64)

        self.reset()

    @staticmethod
    def getInstance() -> "Game":
        return Game._instance

    @property
    def bat(self):
        return self._bat

    @property
    def pipe_spawner(self):
        return self._pipe_spawner

    @property
    def background(self):
        return self._bg

    def jump(self):
        self.bat.jump()

    def draw(self, screen:Surface):
        self.background.draw(screen)
        self.pipe_spawner.draw_pipes(screen)
        self.bat.draw(screen)

        score_text = self._font.render(str(self._score), True, (140, 0, 0))
        score_text_rect = score_text.get_rect()    
        score_text_rect.center = (SCREEN_SIZE[0]/2 + 3, SCREEN_SIZE[1]/7 + 3)
        screen.blit(score_text, score_text_rect)
        score_text = self._font.render(str(self._score), True, (240, 100, 100))
        score_text_rect.center = (SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/7)
        screen.blit(score_text, score_text_rect)

    def tick(self):
        self.background.tick()
        self.pipe_spawner.tick()
        self.bat.tick()

        if self._reset_timer_limit < 0:
            return
            
        self._reset_counter += 1

        if self._reset_counter >= self._reset_timer_limit:
            self.reset()

    def score(self):
        self._score += 1

    def reset(self):
        self._bat = Bat.getInstance() if Bat.getInstance() is not None else Bat(2*SCREEN_SIZE[0]/5, SCREEN_SIZE[1]/3)
        self.bat.reset()
        self._pipe_spawner = PipeSpawner.getInstance() if PipeSpawner.getInstance() is not None else PipeSpawner(spawn_interval_ms=3000, starting_velocity=140, accelerate_interval_ms=5000, accelerate_amount=3)
        self.pipe_spawner.reset()
        self._bg = Background(
            layer_image_paths=["./assets/background/landscape_0005_6_background.png",
                                "./assets/background/landscape_0004_5_clouds.png",
                                "./assets/background/landscape_0003_4_mountain.png",
                                "./assets/background/landscape_0002_3_trees.png",
                                "./assets/background/landscape_0001_2_trees.png",
                                "./assets/background/landscape_0000_1_trees.png"],
            layer_speed_multipliers=[0.1, 0.15, 0.2, 0.3, 0.5, 0.7]
            )

        self._score = 0

        self._reset_counter = 0
        self._reset_timer_limit = -1


    def restart(self, wait_time_ms):
        self._reset_timer_limit = wait_time_ms/1000 * CLOCK_FREQUENCY