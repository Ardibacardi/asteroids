import pygame
from constants import *
from player import *

def main():
    pygame.init
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2, )

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        player.update(dt)
        
        screen.fill(000000)
        player.draw(screen)
        pygame.display.flip()

        # set fps limit
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()