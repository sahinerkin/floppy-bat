import pygame
from bat import Bat
from pipe import Pipe, PipeType

pygame.init()

screen_size = (400, 700)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Floppy Bat")
clock = pygame.time.Clock()

def main():
    run = True
    my_bat = Bat(2*screen_size[0]/5, screen_size[1]/3)
    my_pipe = Pipe(pos_x=500, length=200, type=PipeType.TOP_PIPE)
    my_pipe2 = Pipe(pos_x=500, length=200, type=PipeType.BOTTOM_PIPE)
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

        my_pipe.draw(screen)
        my_pipe2.draw(screen)
        my_bat.draw(screen)

        pygame.display.flip()

        my_bat.tick()
        my_pipe.tick()
        my_pipe2.tick()
        clock.tick(60)
    

if __name__ == "__main__":
    main()