import pygame
from game import Game
from constants import CLOCK_FREQUENCY, SCREEN_SIZE

pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)
screen.set_alpha(pygame.SRCALPHA)
pygame.display.set_caption("Floppy Bat")
clock = pygame.time.Clock()

my_game = Game()

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    my_game.jump()
            if event.type == pygame.MOUSEBUTTONDOWN:
                my_game.jump()

        screen.fill((0, 255, 255))

        my_game.draw(screen)

        pygame.display.flip()

        my_game.tick()

        clock.tick(CLOCK_FREQUENCY)
    

if __name__ == "__main__":
    main()