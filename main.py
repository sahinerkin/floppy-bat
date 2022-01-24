import pygame
from background import Background
from bat import Bat
from pipe_spawner import PipeSpawner
from constants import CLOCK_FREQUENCY, SCREEN_SIZE

pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)
screen.set_alpha(pygame.SRCALPHA)
pygame.display.set_caption("Floppy Bat")
clock = pygame.time.Clock()
my_bat = Bat(2*SCREEN_SIZE[0]/5, SCREEN_SIZE[1]/3)
my_spawner = PipeSpawner(spawn_interval_ms=3000, starting_velocity=140, accelerate_interval_ms=5000, accelerate_amount=3)
my_bg = Background(
    layer_image_paths=["./assets/background/landscape_0005_6_background.png",
                       "./assets/background/landscape_0004_5_clouds.png",
                       "./assets/background/landscape_0003_4_mountain.png",
                       "./assets/background/landscape_0002_3_trees.png",
                       "./assets/background/landscape_0001_2_trees.png",
                       "./assets/background/landscape_0000_1_trees.png"],
    layer_speed_multipliers=[0.1, 0.15, 0.2, 0.3, 0.5, 0.7]
    )

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    my_bat.jump()
            if event.type == pygame.MOUSEBUTTONDOWN:
                my_bat.jump()

        screen.fill((0, 255, 255))

        my_bg.draw(screen)
        my_bat.draw(screen)
        my_spawner.draw_pipes(screen)

        pygame.display.flip()

        my_bg.tick()
        my_bat.tick()
        my_spawner.tick()

        clock.tick(CLOCK_FREQUENCY)
    

if __name__ == "__main__":
    main()