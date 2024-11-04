import pygame
from constants import *
from player import *

def main():
    pygame.init
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2, )

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updatable:    
            obj.update(dt)

        screen.fill(000000)
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # set fps limit
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()