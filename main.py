import pygame
from bat import Bat
from pipe_spawner import PipeSpawner
from constants import CLOCK_FREQUENCY, SCREEN_SIZE

pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)
screen.set_alpha(pygame.SRCALPHA)
pygame.display.set_caption("Floppy Bat")
clock = pygame.time.Clock()
my_bat = Bat(2*SCREEN_SIZE[0]/5, SCREEN_SIZE[1]/3)

my_gen = PipeSpawner(spawn_interval_ms=3000, starting_velocity=140, accelerate_interval_ms=5000, accelerate_amount=3)

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

        my_gen.draw_pipes(screen)
        my_bat.draw(screen)
        my_bat.tick()
        my_gen.tick()

        pygame.display.flip()



        clock.tick(CLOCK_FREQUENCY)
    

if __name__ == "__main__":
    main()