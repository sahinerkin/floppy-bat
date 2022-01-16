import pygame
from birb import Birb

pygame.init()

screen_size = (400, 700)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Floppy Birb")
clock = pygame.time.Clock()

def main():
    run = True
    my_birb = Birb(screen_size[0]/2, screen_size[1]/3)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    my_birb.jump()
            if event.type == pygame.MOUSEBUTTONDOWN:
                my_birb.jump()

        screen.fill((0, 255, 255))
        my_birb.draw(screen)
        pygame.display.flip()
        my_birb.tick()
        clock.tick(60)
    

if __name__ == "__main__":
    main()