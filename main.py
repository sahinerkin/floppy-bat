import pygame
from bat import Bat
from pipe import Pipe, PipeType

pygame.init()

screen_size = (400, 700)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Floppy Bat")
clock = pygame.time.Clock()
my_bat = Bat(2*screen_size[0]/5, screen_size[1]/3)

def main():
    run = True
    pipes = []
    i = 0
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

        if i == 120:
            my_pipe = Pipe(pos_x=500, length=200, velocity=2, type=PipeType.TOP_PIPE)
            my_pipe2 = Pipe(pos_x=500, length=200, velocity=2, type=PipeType.BOTTOM_PIPE)
            pipes += [my_pipe, my_pipe2]
            i = 0
        
        for pipe in pipes:
            pipe.draw(screen)

        my_bat.draw(screen)

        pygame.display.flip()

        for pipe in pipes:
            pipe.tick()

        my_bat.tick()
        clock.tick(60)
        i += 1
    

if __name__ == "__main__":
    main()