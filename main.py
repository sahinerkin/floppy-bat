import pygame
from bat import Bat
from pipe_generator import PipeGenerator
from constants import CLOCK_FREQUENCY, SCREEN_SIZE

pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)
screen.set_alpha(pygame.SRCALPHA)
pygame.display.set_caption("Floppy Bat")
clock = pygame.time.Clock()
my_bat = Bat(2*SCREEN_SIZE[0]/5, SCREEN_SIZE[1]/3)
my_gen = PipeGenerator(time_interval_ms=3000)

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


        pygame.display.flip()

        my_bat.tick()
        my_gen.tick()

        clock.tick(CLOCK_FREQUENCY)
    

if __name__ == "__main__":
    main()